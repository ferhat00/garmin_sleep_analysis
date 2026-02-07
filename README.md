# 🌙 Garmin Sleep Analysis Project

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Last Updated](https://img.shields.io/badge/updated-February%202026-brightgreen.svg)

A comprehensive personal sleep quality analysis project using 5+ years of Garmin wearable device data. This project performs exploratory data analysis (EDA) on sleep patterns, architecture, and temporal trends to derive actionable health insights.

**Patient:** Ferhat  
**Analysis Period:** January 2021 - February 2026  
**Total Nights Analyzed:** 1,353  
**ZOE Microbiome Score:** 84 (Very High)

---

## 📋 Table of Contents

- [Privacy & Disclaimer](#-privacy--disclaimer)
- [Project Overview](#-project-overview)
- [Version History](#-version-history)
- [Features](#-features)
- [Installation](#-installation)
- [Data Structure](#-data-structure)
- [Usage](#-usage)
- [Analysis Sections](#-analysis-sections)
- [Key Findings](#-key-findings)
- [Sample Visualizations](#-sample-visualizations)
- [Outputs](#-outputs)
- [Technologies](#-technologies)
- [Limitations](#-limitations)
- [Future Work](#-future-work)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🔒 Privacy & Disclaimer

### Personal Health Data Notice

⚠️ **IMPORTANT:** This repository contains personal health data analysis for individual use only.

- The sleep data files (`*_sleepData.json`) contain **personal biometric information** exported from Garmin Connect
- This project is designed for **personal health tracking and self-analysis**
- **No medical advice:** This analysis is for informational purposes only and should not replace professional medical consultation
- **Data privacy:** If you fork this repository, ensure you replace all JSON data files with your own Garmin exports before sharing

### For Others Using This Code

✅ **You are welcome to:**
- Fork this repository for your own personal sleep analysis
- Use the notebook and scripts with your own Garmin Connect data
- Modify and extend the analysis for your needs

❌ **Please do not:**
- Use this code for medical diagnosis or treatment decisions
- Share personal health data publicly
- Claim this as clinical or research-grade analysis

### How to Use With Your Own Data

1. Export your sleep data from [Garmin Connect](https://connect.garmin.com) (Account Settings → Export Data → Sleep)
2. Replace the `*_sleepData.json` files in the `v3/` folder with your exports
3. Update the metadata in the notebook (patient name, ZOE score, etc.)
4. Run the analysis notebook to generate your personalized insights

---

## 📊 Project Overview

This project analyzes **5+ years of continuous sleep tracking data** from a Garmin wearable device to understand:

- **Sleep Duration Patterns:** Daily, weekly, monthly, and seasonal trends
- **Sleep Architecture:** Deep sleep, light sleep, REM, and awake time distribution
- **Sleep Efficiency:** Time asleep vs. time in bed
- **Temporal Correlations:** Relationships between sleep metrics
- **Health Insights:** Connection to gut microbiome health (ZOE Program)

### Why This Project?

Personal health data tracking provides:
- ✅ Data-driven insights into sleep quality over extended periods
- ✅ Identification of patterns and trends not visible day-to-day
- ✅ Objective metrics to optimize sleep hygiene
- ✅ Historical baseline for detecting changes
- ✅ Correlation analysis with other health metrics (e.g., ZOE microbiome score)

---

## 📚 Version History

This project has evolved through three major versions:

### v1 (Initial Analysis)
- **Scope:** Basic exploratory analysis
- **Data Period:** Limited to 1-2 years
- **Features:**
  - Simple data loading from JSON files
  - Basic descriptive statistics
  - Initial time series visualizations
  - Sleep duration distributions
- **Limitations:** Limited temporal analysis, no seasonal patterns, basic visualizations

### v2 (Expanded Analysis)
- **Scope:** Enhanced EDA with more metrics
- **Data Period:** 2-3 years of data
- **Features:**
  - Improved data preprocessing pipeline
  - Sleep architecture breakdown (deep/light/awake)
  - Day-of-week pattern analysis
  - Sleep efficiency calculations
  - Enhanced visualizations with seaborn
  - Monthly trend analysis
- **Improvements:** Better data quality filtering, additional calculated metrics, professional chart styling

### v3 (Comprehensive Analysis) - **CURRENT**
- **Scope:** Complete 5+ year longitudinal analysis
- **Data Period:** January 2021 - February 2026 (1,353 nights)
- **Features:**
  - ✨ **12 comprehensive analysis sections**
  - ✨ Full sleep architecture analysis (deep, light, REM, awake)
  - ✨ Seasonal pattern detection (Winter, Spring, Summer, Autumn)
  - ✨ Rolling 30-day averages for trend smoothing
  - ✨ Correlation matrix and statistical relationships
  - ✨ Clinical insights and health recommendations
  - ✨ ZOE microbiome score integration
  - ✨ Data quality filtering (OFF_WRIST detection)
  - ✨ Professional HTML export capability
  - ✨ Processed CSV output for further analysis
- **Data Source:** 25 JSON files covering extended period (April 2019 - February 2026)
- **Improvements:** Significantly expanded temporal coverage, clinical interpretation, gut health correlation, publication-quality visualizations

### Why Maintain Separate Versions?

Each version folder is preserved to:
1. **Track Evolution:** Document how the analysis approach matured over time
2. **Reproducibility:** Maintain original analyses with their specific data periods
3. **Experimentation:** Allow comparison of different methodologies
4. **Learning:** Serve as examples of progressive complexity in data analysis

**Recommendation:** Use **v3** for current and future analyses as it represents the most comprehensive and refined approach.

---

## ✨ Features

### Data Processing
- ✅ Automated loading of multiple JSON data files
- ✅ Timestamp conversion and timezone handling
- ✅ Duration calculations (seconds → hours)
- ✅ Sleep efficiency calculation: `(total sleep / time in bed) × 100`
- ✅ Sleep architecture percentages (deep, light, awake)
- ✅ Data quality filtering (removes OFF_WRIST sessions)
- ✅ Temporal feature engineering (day of week, month, season, year, quarter)
- ✅ 30-day rolling averages for trend analysis

### Analysis Capabilities
- 📈 **Time Series Analysis:** Daily sleep patterns with trend detection
- 📊 **Descriptive Statistics:** Mean, median, standard deviation, percentiles
- 🗓️ **Temporal Patterns:** Day-of-week, monthly, seasonal, yearly comparisons
- 🧠 **Sleep Architecture:** Deep vs. light sleep distribution and trends
- 🔗 **Correlation Analysis:** Relationships between sleep metrics
- 💤 **Sleep Efficiency:** Quality metrics and compliance with optimal ranges (7-9 hours)
- 🏥 **Clinical Insights:** Health implications and personalized recommendations

### Visualizations
- 📉 Line charts with rolling averages
- 📊 Bar charts for categorical comparisons
- 🥧 Pie charts for sleep architecture
- 🔥 Correlation heatmaps
- 📐 Distribution histograms
- 📅 Seasonal comparison plots

---

## 🚀 Installation

### Prerequisites
- **Python 3.8+** (tested on Python 3.14)
- **Jupyter Notebook** or **JupyterLab**
- **Garmin Connect Account** (for exporting your own data)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/garmin_sleep_analysis.git
   cd garmin_sleep_analysis
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - `pandas>=1.3.0` - Data manipulation
   - `numpy>=1.21.0` - Numerical operations
   - `matplotlib>=3.4.0` - Basic plotting
   - `seaborn>=0.11.0` - Statistical visualizations
   - `scipy>=1.7.0` - Statistical analysis
   - `jupyter>=1.0.0` - Notebook environment

4. **Verify Installation**
   ```bash
   python -c "import pandas, numpy, matplotlib, seaborn, scipy; print('✓ All packages installed')"
   ```

### Exporting Garmin Sleep Data

To use this analysis with your own Garmin data:

1. **Log in to Garmin Connect Web**
   - Visit [https://connect.garmin.com](https://connect.garmin.com)
   - Sign in with your Garmin account

2. **Navigate to Export Settings**
   - Click on your profile icon (top right)
   - Select **Account Settings**
   - Go to **Data Management** → **Export Your Data**

3. **Request Sleep Data Export**
   - Select date range (e.g., past 5 years)
   - Choose **Sleep Data** category
   - Click **Request Export**

4. **Download and Place Files**
   - Garmin will send a download link via email
   - Download the ZIP file
   - Extract JSON files to `v3/` folder
   - Files will be named: `YYYY-MM-DD_YYYY-MM-DD_[UserID]_sleepData.json`

5. **Update Notebook**
   - Open `v3/Sleep_Analysis_Complete_EDA.ipynb`
   - Update the `json_files` list with your file names
   - Modify metadata (patient name, ZOE score, etc.)

---

## 📁 Data Structure

### Raw JSON Format

Each Garmin sleep data file is a JSON array containing sleep records:

```json
[
  {
    "sleepStartTimestampGMT": "2024-06-14T22:09:00.0",
    "sleepEndTimestampGMT": "2024-06-15T06:08:00.0",
    "calendarDate": "2024-06-15",
    "sleepWindowConfirmationType": "ENHANCED_CONFIRMED_FINAL",
    "deepSleepSeconds": 4800,
    "lightSleepSeconds": 20940,
    "remSleepSeconds": 3000,
    "awakeSleepSeconds": 0,
    "unmeasurableSeconds": 0,
    "retro": false
  }
]
```

#### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `sleepStartTimestampGMT` | ISO 8601 String | Sleep session start time (GMT) |
| `sleepEndTimestampGMT` | ISO 8601 String | Sleep session end time (GMT) |
| `calendarDate` | Date String | Calendar date of the sleep session |
| `sleepWindowConfirmationType` | String | Validation status of sleep detection |
| `deepSleepSeconds` | Integer | Total deep sleep duration (seconds) |
| `lightSleepSeconds` | Integer | Total light sleep duration (seconds) |
| `remSleepSeconds` | Integer | Total REM sleep duration (seconds) |
| `awakeSleepSeconds` | Integer | Total awake time during sleep window (seconds) |
| `unmeasurableSeconds` | Integer | Time with insufficient data (seconds) |
| `retro` | Boolean | Whether sleep was retroactively detected |

#### Sleep Window Confirmation Types

| Type | Description | Quality |
|------|-------------|---------|
| `ENHANCED_CONFIRMED_FINAL` | Validated with enhanced detection, finalized | ⭐⭐⭐⭐⭐ Highest |
| `ENHANCED_CONFIRMED` | Validated with enhanced detection | ⭐⭐⭐⭐ High |
| `AUTO_CONFIRMED_FINAL` | Auto-detected, finalized | ⭐⭐⭐ Good |
| `AUTO_CONFIRMED` | Auto-detected | ⭐⭐ Fair |
| `UNCONFIRMED` | Not validated | ⭐ Low |
| `OFF_WRIST` | Device not worn (filtered out) | ❌ Invalid |

### Processed CSV Format

The notebook generates a processed CSV file (`v3/outputs/sleep_data_processed.csv`) with **33 columns**:

#### Original Fields (10 columns)
- Raw timestamp and duration fields from JSON

#### Calculated Metrics (15 columns)
- `deepSleepHours`, `lightSleepHours`, `awakeHours` - Converted to hours
- `totalSleepHours` - Sum of deep + light sleep
- `totalTimeInBedHours` - Time from sleep start to sleep end
- `sleepEfficiency` - Percentage: `(total sleep / time in bed) × 100`
- `deepSleepPercentage` - Percentage: `(deep sleep / total sleep) × 100`
- `lightSleepPercentage` - Percentage: `(light sleep / total sleep) × 100`
- And more...

#### Temporal Features (8 columns)
- `dayOfWeek` - Monday, Tuesday, etc.
- `month` - 1-12
- `season` - Winter, Spring, Summer, Autumn
- `year` - 2021, 2022, etc.
- `quarter` - Q1, Q2, Q3, Q4
- `weekOfYear` - 1-52
- `rolling_avg_30d` - 30-day rolling average of sleep duration

---

## 💻 Usage

### Running the Analysis

1. **Launch Jupyter Notebook**
   ```bash
   cd v3
   jupyter notebook Sleep_Analysis_Complete_EDA.ipynb
   ```
   Or use JupyterLab:
   ```bash
   jupyter lab Sleep_Analysis_Complete_EDA.ipynb
   ```

2. **Run All Cells**
   - Click **Kernel** → **Restart & Run All**
   - Or press `Shift + Enter` to run cells sequentially

3. **Review Results**
   - Scroll through the notebook to see visualizations
   - Check the **Clinical Summary** section at the end for key insights

### Generating HTML Export

To create a shareable HTML report:

1. **In Jupyter Notebook**
   - Click **File** → **Download as** → **HTML (.html)**

2. **Using nbconvert (Command Line)**
   ```bash
   jupyter nbconvert --to html Sleep_Analysis_Complete_EDA.ipynb
   ```

3. **Result**
   - `Sleep_Analysis_Complete_EDA.html` will be created
   - Open in any web browser to view the complete analysis

### Accessing Processed Data

The processed CSV file can be used for further analysis:

```python
import pandas as pd

# Load processed data
df = pd.read_csv('v3/outputs/sleep_data_processed.csv')

# Your custom analysis here
print(df.describe())
```

---

## 🔬 Analysis Sections

The notebook consists of 12 comprehensive sections:

### 1. Data Loading
- Loads 19 JSON files covering the analysis period
- Combines data into a single DataFrame
- Displays initial data structure

### 2. Data Preprocessing
- Converts timestamps to datetime objects
- Calculates sleep durations in hours
- Derives sleep efficiency and architecture percentages
- Filters out OFF_WRIST and invalid sessions
- Adds temporal features (day of week, month, season, etc.)

### 3. Descriptive Statistics & KPIs
- **Sleep Duration:** Mean, median, std, min, max
- **Sleep Architecture:** Average deep/light/awake breakdown
- **Sleep Efficiency:** Average, range, compliance with optimal
- **Key Performance Indicators:**
  - Average sleep duration: ~7.2 hours
  - Sleep efficiency: ~96% (excellent)
  - Deep sleep percentage: ~53% (unusually high - see limitations)
  - Nights meeting 7-9 hour target: ~X%

### 4. Sleep Duration Analysis
- Time series plot with 30-day rolling average
- Distribution histogram
- Comparison to optimal range (7-9 hours)
- Trend detection over 5 years

### 5. Sleep Architecture Analysis
- Pie chart of average sleep composition
- Deep vs. light sleep over time
- Sleep stage trends
- Stage percentage distributions

### 6. Day of Week Patterns
- Average sleep by weekday (Monday-Sunday)
- Weekend vs. weekday comparison
- Sleep efficiency by day
- Consistency analysis

### 7. Monthly Patterns
- Average sleep duration by month (Jan-Dec)
- Seasonal clustering
- Year-over-year monthly comparisons

### 8. Seasonal Analysis
- Sleep patterns by season (Winter, Spring, Summer, Autumn)
- Seasonal sleep efficiency comparison
- Temperature and daylight impact inference

### 9. Sleep Timing Analysis
- Bedtime distribution
- Wake time distribution
- Bedtime vs. wake time correlation
- Sleep schedule consistency metrics

### 10. Sleep Efficiency Trends
- Efficiency over time
- Efficiency distribution
- Seasonal efficiency comparison
- Factors affecting efficiency

### 11. Correlation Analysis
- Correlation heatmap of all sleep metrics
- Scatter plots for key relationships:
  - Total sleep vs. deep sleep
  - Sleep efficiency vs. awake time
  - Deep sleep percentage vs. total sleep
  - Bedtime vs. wake time

### 12. Clinical Summary & Recommendations
- **Key Findings:** Summary of 5-year patterns
- **Strengths:** What's working well (e.g., high efficiency)
- **Areas for Improvement:** Actionable recommendations
- **Health Connections:** Relationship to ZOE microbiome score (84 - Very High)
- **Personalized Recommendations:** Sleep hygiene tips based on data

---

## 🔑 Key Findings

Based on 1,353 nights of sleep data (January 2021 - February 2026):

### ✅ Strengths

1. **Excellent Sleep Efficiency**
   - Average: ~96%
   - Indicates high-quality sleep with minimal wakefulness
   - Well above the 85% threshold for good sleep quality

2. **Consistent Patterns**
   - Regular sleep-wake cycle maintained over 5+ years
   - Low variance in bedtime and wake time
   - Strong circadian rhythm adherence

3. **Positive Health Correlation**
   - ZOE microbiome score: 84 (Very High)
   - Suggests strong gut-brain axis connection
   - Sleep quality may contribute to microbiome health

### ⚠️ Areas for Improvement

1. **Sleep Duration**
   - Average: ~7.2 hours
   - Slightly below optimal 7.5-9 hour range for adults
   - **Recommendation:** Aim for 30 minutes additional sleep

2. **Deep Sleep Percentage**
   - Average: ~53% of total sleep
   - Unusually high (typical: 15-25%)
   - **Note:** Likely due to Garmin algorithm combining deep + REM stages
   - See [Limitations](#-limitations) section

3. **Weekend Catch-up Pattern**
   - Slightly longer sleep on weekends
   - Indicates weekday sleep debt
   - **Recommendation:** More consistent weekday sleep schedule

### 📈 Trends Over Time

- **Overall Duration:** Stable with minor seasonal variations
- **Seasonal Pattern:** Slightly more sleep in winter months (~15 min)
- **Sleep Efficiency:** Consistently high across all seasons
- **Year-over-Year:** No significant degradation (positive sign)

### 🔗 Correlations Discovered

| Relationship | Correlation | Interpretation |
|--------------|-------------|----------------|
| Total Sleep ↔ Deep Sleep | Strong Positive | More sleep = more deep sleep |
| Sleep Efficiency ↔ Awake Time | Strong Negative | Less awake time = higher efficiency |
| Bedtime ↔ Wake Time | Moderate Positive | Later bedtime = later wake time |
| Deep Sleep % ↔ Total Sleep | Weak Positive | Longer sleep slightly increases deep % |

---

## 🖼️ Sample Visualizations

### Sleep Duration Over Time
![Sleep Duration Time Series](assets/images/sleep_duration_timeseries.png)
*5-year time series showing daily sleep duration (blue dots) with 30-day rolling average (dark blue line). Green and orange dashed lines indicate optimal sleep range (7-9 hours).*

### Sleep Architecture
![Sleep Architecture](assets/images/sleep_architecture.png)
*Average composition of sleep: Deep sleep (~3.8h, 53%), Light sleep (~3.3h, 46%), Awake time (~0.1h, 1%). Note: Garmin may combine deep + REM into "deep sleep" category.*

### Day of Week Patterns
![Day of Week Patterns](assets/images/day_of_week_patterns.png)
*Average sleep duration by day of week. Weekend effect visible with slightly longer sleep on Saturdays and Sundays.*

### Seasonal Patterns
![Seasonal Patterns](assets/images/seasonal_patterns.png)
*Sleep duration variations across seasons. Winter shows slightly higher average sleep duration (~15 minutes more than summer).*

### Correlation Heatmap
![Correlation Heatmap](assets/images/correlation_heatmap.png)
*Correlation matrix showing relationships between sleep metrics. Strong positive correlation between total sleep and deep sleep; strong negative correlation between sleep efficiency and awake time.*

---

## 📤 Outputs

The analysis generates the following outputs:

### 1. Processed CSV File
- **Location:** `v3/outputs/sleep_data_processed.csv`
- **Rows:** 1,353 (one per night)
- **Columns:** 33 (original + calculated + temporal features)
- **Use Cases:**
  - Import into Excel/Google Sheets for further analysis
  - Use with other data science tools (R, Tableau, etc.)
  - Merge with other health data (activity, nutrition, etc.)

### 2. HTML Report
- **Location:** `v3/Sleep_Analysis_Complete_EDA.html`
- **Contents:** Complete notebook with all visualizations
- **Use Cases:**
  - Share with healthcare providers
  - Archive for future reference
  - View without running Jupyter

### 3. Visualization Images
- **Location:** `assets/images/`
- **Files:**
  - `sleep_duration_timeseries.png`
  - `sleep_architecture.png`
  - `day_of_week_patterns.png`
  - `seasonal_patterns.png`
  - `correlation_heatmap.png`
- **Format:** PNG (300 DPI, publication quality)
- **Use Cases:** Presentations, reports, documentation

---

## 🛠️ Technologies

### Programming Languages
- **Python 3.8+** - Core analysis language

### Data Analysis Libraries
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing

### Visualization Libraries
- **matplotlib** - Core plotting library
- **seaborn** - Statistical data visualization (built on matplotlib)

### Statistical Analysis
- **scipy** - Scientific computing and statistics

### Development Environment
- **Jupyter Notebook** - Interactive computing environment
- **IPython** - Enhanced Python shell

### Data Format
- **JSON** - Garmin Connect export format

### Version Control
- **Git** - Source code management

---

## ⚠️ Limitations

### 1. Data Quality

**Device Accuracy**
- Garmin wearables use motion and heart rate sensors, not medical-grade polysomnography
- Sleep stage detection is algorithmic and may have ~10-20% error rate
- OFF_WRIST sessions and UNCONFIRMED data are filtered but may introduce gaps

**Missing Data**
- Days when device wasn't worn are excluded
- Battery death or syncing issues can create gaps
- Naps are not consistently captured (primarily nighttime sleep)

### 2. Sleep Architecture Measurement

**Deep Sleep Percentage Anomaly**
- Observed average: ~53% (unusually high)
- Typical healthy adult: 15-25% deep sleep
- **Likely Cause:** Garmin may combine Deep + REM stages into "deep sleep"
- **Impact:** Sleep architecture percentages should be interpreted cautiously

**No REM Data**
- Older Garmin models don't separate REM sleep
- Analysis focuses on deep/light/awake only

### 3. Analysis Limitations

**Causation vs. Correlation**
- Correlations identified do not imply causation
- External factors (stress, diet, exercise) not accounted for
- Cannot establish cause-effect relationships

**Personal Data Only**
- Analysis is for one individual (Ferhat)
- Results may not generalize to other people
- No control group or comparison data

**Clinical Interpretation**
- This is **not a medical diagnosis**
- Sleep disorders require professional sleep study (polysomnography)
- Consult a healthcare provider for sleep concerns

### 4. Technical Limitations

**Computational**
- Notebook designed for personal analysis (not scalable to large populations)
- No database backend (all data in memory)
- Limited to single-machine processing

**Statistical**
- Basic descriptive statistics and correlation analysis
- No advanced modeling (time series forecasting, anomaly detection, machine learning)
- No hypothesis testing or p-value calculations

### 5. Privacy Considerations

**Personal Health Data**
- Contains identifiable biometric information
- Should not be shared publicly without anonymization
- GDPR/HIPAA considerations for public repositories

---

## 🚀 Future Work

### Planned Enhancements

#### 1. Advanced Analytics
- [ ] **Time Series Forecasting:** Predict future sleep patterns using ARIMA or Prophet
- [ ] **Anomaly Detection:** Automatically flag unusual sleep sessions
- [ ] **Sleep Quality Score:** Composite metric combining duration, efficiency, and architecture
- [ ] **Statistical Testing:** Add hypothesis tests for seasonal differences, trends

#### 2. Data Integration
- [ ] **Activity Data:** Correlate with Garmin activity/step data
- [ ] **Nutrition Data:** Integrate meal timing and dietary patterns (e.g., ZOE app data)
- [ ] **Environmental Data:** Add weather, temperature, light exposure
- [ ] **Stress Metrics:** Include Garmin stress scores and HRV

#### 3. Visualization Improvements
- [ ] **Interactive Dashboards:** Build Plotly/Dash interactive visualizations
- [ ] **Web Application:** Create Flask/Streamlit app for real-time analysis
- [ ] **Mobile-Friendly Reports:** Responsive HTML templates
- [ ] **Animation:** Create animated time series GIFs

#### 4. Machine Learning
- [ ] **Classification:** Predict "good" vs. "bad" sleep nights
- [ ] **Clustering:** Identify distinct sleep pattern phenotypes
- [ ] **Feature Importance:** Determine which factors most impact sleep quality
- [ ] **Recommendation Engine:** Personalized sleep optimization suggestions

#### 5. Automation
- [ ] **Automated Data Import:** Direct API connection to Garmin Connect
- [ ] **Scheduled Analysis:** Cron job for weekly/monthly report generation
- [ ] **Email Alerts:** Notifications for concerning patterns
- [ ] **CI/CD Pipeline:** Automated testing and report generation

#### 6. Documentation
- [ ] **Video Tutorial:** Walkthrough of analysis for new users
- [ ] **Case Studies:** Examples with different sleep patterns
- [ ] **Troubleshooting Guide:** Common issues and solutions
- [ ] **Contributing Guide:** How others can improve the project

### Research Questions

Potential areas for deeper investigation:

1. **What is the optimal sleep duration for maximum next-day productivity?**
   - Requires integration with performance/mood tracking

2. **Do dietary patterns affect sleep quality?**
   - Correlation with ZOE meal logging data

3. **How do exercise timing and intensity impact sleep?**
   - Merge with Garmin activity data

4. **Can we predict poor sleep nights in advance?**
   - Machine learning on multi-day feature windows

5. **What is the relationship between sleep consistency and health outcomes?**
   - Longitudinal analysis with health markers

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Ferhat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### What This Means

✅ **You CAN:**
- Use this code for personal or commercial projects
- Modify and distribute the code
- Use for educational purposes
- Fork and create derivative works

❌ **You CANNOT:**
- Hold the author liable for any issues
- Use the author's name for endorsement without permission

📝 **You MUST:**
- Include the original license and copyright notice in any copies

---

## 🙏 Acknowledgments

### Tools & Services

- **Garmin** - For creating excellent wearable devices and providing data export functionality
- **ZOE Health Study** - For microbiome analysis and personalized nutrition insights
- **Jupyter Project** - For the incredible notebook environment
- **Python Community** - For open-source data science libraries (pandas, matplotlib, seaborn)

### Inspiration

- The **Quantified Self** movement for promoting personal data tracking
- **Matthew Walker** (*Why We Sleep*) - For raising awareness about sleep health importance
- The **open science** community for encouraging data transparency and reproducibility

### Contributing

While this is a personal health project, feedback and suggestions are welcome!

- **Found a bug?** Open an issue describing the problem
- **Have a feature idea?** Submit an issue with the enhancement tag
- **Want to contribute code?** Fork the repository and submit a pull request

**Note:** Since this repository contains personal health data, external contributions are limited to code improvements only. If you use this for your own data analysis, please fork and create your own repository.

---

## 📧 Contact

For questions, feedback, or collaboration inquiries:

- **GitHub Issues:** [Create an issue](https://github.com/yourusername/garmin_sleep_analysis/issues)
- **Email:** your.email@example.com (update with your contact)

---

## 🌟 Star This Repository

If you find this project useful for your own sleep analysis, please consider:
- ⭐ Starring this repository
- 🍴 Forking it for your own use
- 📢 Sharing it with others interested in personal health tracking

---

<div align="center">

**Made with ❤️ for better sleep and data-driven health insights**

*Last Updated: February 5, 2026*

</div>

