"""
Loan Default Analysis - Step 1: Data Cleaning & Exploratory Data Analysis
Author: Lokeshwaran K
Tools: Python (Pandas, NumPy, Matplotlib, Seaborn)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------
df = pd.read_csv("loan_default.csv")

print("Shape of dataset:", df.shape)
print("\nColumn info:")
print(df.info())

print("\nFirst 5 rows:")
print(df.head())

# ---------------------------------------------------------
# 2. Check for missing values & duplicates
# ---------------------------------------------------------
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# Drop duplicates if any (dataset is generally clean, but good practice)
df = df.drop_duplicates()

# ---------------------------------------------------------
# 3. Basic statistics
# ---------------------------------------------------------
print("\nSummary statistics (numeric columns):")
print(df.describe())

print("\nOverall default rate:")
print(df["Default"].value_counts(normalize=True) * 100)

# ---------------------------------------------------------
# 4. Feature engineering - useful groupings for analysis
# ---------------------------------------------------------
# Age bands
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 70],
    labels=["18-25", "26-35", "36-45", "46-55", "56-69"]
)

# Income bands
df["IncomeGroup"] = pd.cut(
    df["Income"],
    bins=[0, 30000, 60000, 90000, 120000, 200000],
    labels=["<30K", "30-60K", "60-90K", "90-120K", "120K+"]
)

# ---------------------------------------------------------
# 5. Default rate by key dimensions
# ---------------------------------------------------------
def default_rate_by(col):
    result = df.groupby(col)["Default"].mean().sort_values(ascending=False) * 100
    return result.round(2)

print("\nDefault rate (%) by Employment Type:")
print(default_rate_by("EmploymentType"))

print("\nDefault rate (%) by Education:")
print(default_rate_by("Education"))

print("\nDefault rate (%) by Age Group:")
print(default_rate_by("AgeGroup"))

print("\nDefault rate (%) by Income Group:")
print(default_rate_by("IncomeGroup"))

print("\nDefault rate (%) by Has Co-Signer:")
print(default_rate_by("HasCoSigner"))

print("\nDefault rate (%) by Has Mortgage:")
print(default_rate_by("HasMortgage"))

print("\nDefault rate (%) by Loan Purpose:")
print(default_rate_by("LoanPurpose"))

# ---------------------------------------------------------
# 6. Correlation between numeric features and Default
# ---------------------------------------------------------
numeric_cols = ["Age", "Income", "LoanAmount", "CreditScore",
                 "MonthsEmployed", "NumCreditLines", "InterestRate",
                 "LoanTerm", "DTIRatio", "Default"]

print("\nCorrelation with Default:")
print(df[numeric_cols].corr()["Default"].sort_values(ascending=False))

# ---------------------------------------------------------
# 7. Save cleaned dataset for SQL / Power BI steps
# ---------------------------------------------------------
df.to_csv("loan_default_cleaned.csv", index=False)
print("\nCleaned file saved as loan_default_cleaned.csv")

# ---------------------------------------------------------
# 8. Visualizations (saved as PNG files)
# ---------------------------------------------------------
sns.set_style("whitegrid")

# Default rate by Employment Type
plt.figure(figsize=(8, 5))
default_rate_by("EmploymentType").plot(kind="bar", color="#1F3864")
plt.title("Default Rate by Employment Type")
plt.ylabel("Default Rate (%)")
plt.tight_layout()
plt.savefig("chart_default_by_employment.png", dpi=150)
plt.close()

# Default rate by Credit Score band
df["CreditScoreBand"] = pd.cut(
    df["CreditScore"],
    bins=[300, 500, 600, 700, 800, 900],
    labels=["300-500", "500-600", "600-700", "700-800", "800+"]
)
plt.figure(figsize=(8, 5))
default_rate_by("CreditScoreBand").sort_index().plot(kind="bar", color="#2E5395")
plt.title("Default Rate by Credit Score Band")
plt.ylabel("Default Rate (%)")
plt.tight_layout()
plt.savefig("chart_default_by_creditscore.png", dpi=150)
plt.close()

# Correlation heatmap
plt.figure(figsize=(9, 7))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("chart_correlation_heatmap.png", dpi=150)
plt.close()

print("\nCharts saved: chart_default_by_employment.png, chart_default_by_creditscore.png, chart_correlation_heatmap.png")
print("\nDone! Next step: load loan_default_cleaned.csv into SQL for query practice.")
