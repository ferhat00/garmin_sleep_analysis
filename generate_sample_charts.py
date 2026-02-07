"""
Generate Sample Visualizations for README
Extracts key charts from the Sleep Analysis notebook
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

print("Loading data...")

# Load all JSON files
json_files = [
    'v3/2020-11-23_2021-03-03_3727308_sleepData.json',
    'v3/2021-03-03_2021-06-11_3727308_sleepData.json',
    'v3/2021-06-11_2021-09-19_3727308_sleepData.json',
    'v3/2021-09-19_2021-12-28_3727308_sleepData.json',
    'v3/2021-12-28_2022-04-07_3727308_sleepData.json',
    'v3/2022-04-07_2022-07-16_3727308_sleepData.json',
    'v3/2022-07-16_2022-10-24_3727308_sleepData.json',
    'v3/2022-10-24_2023-02-01_3727308_sleepData.json',
    'v3/2023-02-01_2023-05-12_3727308_sleepData.json',
    'v3/2023-05-12_2023-08-20_3727308_sleepData.json',
    'v3/2023-08-20_2023-11-28_3727308_sleepData.json',
    'v3/2023-11-28_2024-03-07_3727308_sleepData.json',
    'v3/2024-03-07_2024-06-15_3727308_sleepData.json',
    'v3/2024-06-15_2024-09-23_3727308_sleepData.json',
    'v3/2024-09-23_2025-01-01_3727308_sleepData.json',
    'v3/2025-01-01_2025-04-11_3727308_sleepData.json',
    'v3/2025-04-11_2025-07-20_3727308_sleepData.json',
    'v3/2025-07-20_2025-10-28_3727308_sleepData.json',
    'v3/2025-10-28_2026-02-05_3727308_sleepData.json'
]

all_data = []
for file in json_files:
    try:
        with open(file, 'r') as f:
            all_data.extend(json.load(f))
    except Exception as e:
        print(f"Error loading {file}: {e}")

df = pd.DataFrame(all_data)

# Preprocessing
df['sleepStartTimestamp'] = pd.to_datetime(df['sleepStartTimestampGMT'])
df['sleepEndTimestamp'] = pd.to_datetime(df['sleepEndTimestampGMT'])
df['calendarDate'] = pd.to_datetime(df['calendarDate'])

df['deepSleepHours'] = df['deepSleepSeconds'] / 3600
df['lightSleepHours'] = df['lightSleepSeconds'] / 3600
df['awakeHours'] = df['awakeSleepSeconds'] / 3600
df['totalSleepHours'] = df['deepSleepHours'] + df['lightSleepHours']
df['totalTimeInBedHours'] = (df['sleepEndTimestamp'] - df['sleepStartTimestamp']).dt.total_seconds() / 3600
df['sleepEfficiency'] = (df['totalSleepHours'] / df['totalTimeInBedHours'] * 100).round(1)
df['deepSleepPercentage'] = (df['deepSleepHours'] / df['totalSleepHours'] * 100).round(1)

# Filter data
df_clean = df[
    (df['sleepWindowConfirmationType'] != 'OFF_WRIST') & 
    (df['calendarDate'] >= '2021-01-01')
].copy()

df_clean = df_clean.sort_values('calendarDate').reset_index(drop=True)
df_clean['rolling_avg_30d'] = df_clean['totalSleepHours'].rolling(window=30, min_periods=1).mean()

print(f"Processed {len(df_clean)} records")
print("Generating visualizations...\n")

# 1. Sleep Duration Time Series
print("1/5 Creating sleep duration time series...")
plt.figure(figsize=(14, 6))
plt.plot(df_clean['calendarDate'], df_clean['totalSleepHours'], alpha=0.3, label='Daily Sleep', color='steelblue')
plt.plot(df_clean['calendarDate'], df_clean['rolling_avg_30d'], linewidth=2, label='30-Day Rolling Average', color='darkblue')
plt.axhline(y=7, color='green', linestyle='--', alpha=0.6, label='Optimal Minimum (7h)')
plt.axhline(y=9, color='orange', linestyle='--', alpha=0.6, label='Optimal Maximum (9h)')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sleep (Hours)', fontsize=12)
plt.title('Sleep Duration Over Time (2021-2026)', fontsize=14, fontweight='bold')
plt.legend(loc='upper right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('assets/images/sleep_duration_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Sleep Architecture Pie Chart
print("2/5 Creating sleep architecture pie chart...")
avg_deep = df_clean['deepSleepHours'].mean()
avg_light = df_clean['lightSleepHours'].mean()
avg_awake = df_clean['awakeHours'].mean()

plt.figure(figsize=(8, 8))
sizes = [avg_deep, avg_light, avg_awake]
labels = [f'Deep Sleep\n{avg_deep:.1f}h ({avg_deep/(avg_deep+avg_light+avg_awake)*100:.1f}%)',
          f'Light Sleep\n{avg_light:.1f}h ({avg_light/(avg_deep+avg_light+avg_awake)*100:.1f}%)',
          f'Awake\n{avg_awake:.1f}h ({avg_awake/(avg_deep+avg_light+avg_awake)*100:.1f}%)']
colors = ['#4C72B0', '#55A868', '#C44E52']
explode = (0.05, 0, 0)

plt.pie(sizes, labels=labels, colors=colors, autopct='', startangle=90, explode=explode, textprops={'fontsize': 11})
plt.title('Average Sleep Architecture\n(2021-2026)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('assets/images/sleep_architecture.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Day of Week Patterns
print("3/5 Creating day of week patterns...")
df_clean['dayOfWeek'] = df_clean['calendarDate'].dt.day_name()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_avg = df_clean.groupby('dayOfWeek')['totalSleepHours'].mean().reindex(day_order)

plt.figure(figsize=(10, 6))
bars = plt.bar(range(len(daily_avg)), daily_avg.values, color='steelblue', alpha=0.8)
plt.axhline(y=daily_avg.mean(), color='red', linestyle='--', alpha=0.6, label=f'Weekly Average ({daily_avg.mean():.2f}h)')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Average Sleep (Hours)', fontsize=12)
plt.title('Average Sleep Duration by Day of Week', fontsize=14, fontweight='bold')
plt.xticks(range(len(day_order)), day_order, rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('assets/images/day_of_week_patterns.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Seasonal Patterns
print("4/5 Creating seasonal patterns...")
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df_clean['month'] = df_clean['calendarDate'].dt.month
df_clean['season'] = df_clean['month'].apply(get_season)

season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
seasonal_stats = df_clean.groupby('season')['totalSleepHours'].agg(['mean', 'std']).reindex(season_order)

plt.figure(figsize=(10, 6))
x = range(len(seasonal_stats))
plt.bar(x, seasonal_stats['mean'], yerr=seasonal_stats['std'], capsize=5, color='teal', alpha=0.7)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Average Sleep (Hours)', fontsize=12)
plt.title('Average Sleep Duration by Season', fontsize=14, fontweight='bold')
plt.xticks(x, season_order)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('assets/images/seasonal_patterns.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Correlation Heatmap
print("5/5 Creating correlation heatmap...")
corr_cols = ['totalSleepHours', 'deepSleepHours', 'lightSleepHours', 'awakeHours', 'sleepEfficiency', 'deepSleepPercentage']
corr_matrix = df_clean[corr_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8}, fmt='.2f')
plt.title('Sleep Metrics Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('assets/images/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n✓ All visualizations saved to assets/images/")
print("  - sleep_duration_timeseries.png")
print("  - sleep_architecture.png")
print("  - day_of_week_patterns.png")
print("  - seasonal_patterns.png")
print("  - correlation_heatmap.png")
