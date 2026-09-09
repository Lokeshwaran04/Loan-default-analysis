# Loan Default Analysis

End-to-end data analysis project exploring loan default risk using **Python**, **SQL**, and **Power BI**.

## Problem Statement
Financial institutions need to identify which borrower profiles carry the highest risk of loan default, in order to make better lending decisions and manage risk. This project analyzes historical loan data to uncover the key drivers behind loan defaults.

## Dataset
- **Source:** [Loan Default Prediction Dataset](https://www.kaggle.com/) by nikhil1e9 (Kaggle)
- **Size:** 255,347 rows, 18 columns
- **Note:** The full raw dataset is not included in this repo due to size. A 5,000-row sample (`loan_default_sample.csv`) is provided for reference — download the full dataset from Kaggle to reproduce the analysis.

## Tools Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn) — data cleaning and exploratory analysis
- **SQL** — business-question queries on the cleaned data
- **Power BI** — interactive dashboard for key metrics

## Approach
1. **Data Cleaning:** Checked for missing values and duplicates (dataset was clean); engineered Age Group, Income Group, and Credit Score Band features for analysis.
2. **Exploratory Analysis:** Calculated default rate across employment type, education, age group, income group, co-signer status, mortgage status, and loan purpose.
3. **Correlation Analysis:** Examined which numeric features (age, income, credit score, interest rate, etc.) correlate most with default risk.
4. **Visualization:** Built charts for default rate by employment type, credit score band, and a full correlation heatmap.

## Key Insights
- Overall default rate in the dataset: **11.6%**
- **Age is the strongest driver:** borrowers aged 18–25 default at **20.8%**, versus just **5.5%** for those aged 56–69.
- **Income matters:** borrowers earning under $30K default at **22%**, compared to **9%** for those earning $120K+.
- **Employment type:** Unemployed borrowers have the highest default rate (**13.6%**), Full-time employees the lowest (**9.5%**).
- **Interest rate** shows a mild positive correlation with default (0.13) — higher rates are associated with slightly higher default risk.
- Having a **co-signer** or a **mortgage** is associated with a lower default rate.

## Files in this Repository
| File | Description |
|---|---|
| `01_data_cleaning_eda.py` | Python script for cleaning, feature engineering, and EDA |
| `loan_default_sample.csv` | 5,000-row sample of the cleaned dataset |
| `chart_default_by_employment.png` | Default rate by employment type |
| `chart_default_by_creditscore.png` | Default rate by credit score band |
| `chart_correlation_heatmap.png` | Correlation heatmap of numeric features |

## Author
**Lokeshwaran K**
[LinkedIn](https://www.linkedin.com/in/lokeshwaran-k04)

