123import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "C:\\Users\\TANISH\\Downloads\\12322927-pythonproject\\excelprojectdata.csv"
df = pd.read_csv(file_path)

# Handling missing values
df.fillna(0, inplace=True)

# Summary Statistics
print("Summary Statistics:")
print(df.describe())

# 1. Total Beneficiaries by State
if "state_name" in df.columns and "total_beneficiaries" in df.columns:
    statewise_beneficiaries = df.groupby("state_name")["total_beneficiaries"].sum().reset_index()
    print("\nTotal Beneficiaries by State:")
    print(statewise_beneficiaries)
else:
    print("Columns 'state_name' or 'total_beneficiaries' not found in dataset.")

# 2. Distribution of Beneficiaries
if "total_beneficiaries" in df.columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df["total_beneficiaries"], bins=30, kde=True)
    plt.title("Distribution of Total Beneficiaries")
    plt.xlabel("Total Beneficiaries")
    plt.ylabel("Frequency")
    plt.show()
else:
    print("Column 'total_beneficiaries' not found in dataset.")

# 3. Aadhar vs Mobile Number Correlation
if "total_aadhar" in df.columns and "total_mobileno" in df.columns:
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=df["total_aadhar"], y=df["total_mobileno"], alpha=0.6)
    plt.title("Correlation between Aadhar and Mobile-linked Beneficiaries")
    plt.xlabel("Total Aadhar")
    plt.ylabel("Total Mobile Numbers")
    plt.show()
else:
    print("Columns 'total_aadhar' or 'total_mobileno' not found in dataset.")

# 4. Beneficiary Breakdown by Category
beneficiary_categories = ["total_sc", "total_st", "total_gen", "total_obc"]
available_categories = [col for col in beneficiary_categories if col in df.columns]
if available_categories:
    df[available_categories].sum().plot(kind="bar", figsize=(8,5), color=['blue', 'green', 'red', 'purple'])
    plt.title("Beneficiary Breakdown by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Count")
    plt.xticks(rotation=0)
    plt.show()
else:
    print("None of the category columns found in dataset.")

# 5. State-wise Average Beneficiaries
if "state_name" in df.columns and "total_beneficiaries" in df.columns:
    statewise_avg = df.groupby("state_name")["total_beneficiaries"].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(y="state_name", x="total_beneficiaries", hue="state_name", data=statewise_avg, dodge=False, legend=False, palette="magma")
    plt.title("State-wise Average Beneficiaries")
    plt.xlabel("Average Beneficiaries")
    plt.ylabel("State Name")
    plt.show()
else:
    print("Columns 'state_name' or 'total_beneficiaries' not found in dataset.")
