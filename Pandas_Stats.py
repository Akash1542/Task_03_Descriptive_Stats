#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

# Load the dataset
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_fb_ads_president_scored_anon.csv"  # Update this to your actual file path
df = pd.read_csv(file_path)

# ===== 1. OVERALL STATISTICS =====
print("\n=== Overall Describe ===")
print(df.describe(include='all'))

# Non-numeric column summary
non_numeric = df.select_dtypes(exclude='number')
for col in non_numeric.columns:
    print(f"\n=== {col} Value Counts ===")
    print(df[col].value_counts().head(5))  # Top 5 most frequent values
    print(f"Unique values: {df[col].nunique()}")

# ===== 2. GROUPED BY 'page_id' =====
print("\n\n=== Grouped by 'page_id' ===")
grouped_page = df.groupby('page_id')

# Numerical stats per group
print(grouped_page.describe().transpose())

# Most common non-numeric values per group
for col in non_numeric.columns:
    print(f"\nMost common {col} per page_id:")
    print(grouped_page[col].agg(lambda x: x.value_counts().idxmax()))

# ===== 3. GROUPED BY ['page_id', 'ad_id'] =====
print("\n\n=== Grouped by ['page_id', 'ad_id'] ===")
grouped_page_ad = df.groupby(['page_id', 'ad_id'])

# Numerical stats per group
print(grouped_page_ad.describe().transpose())


import pandas as pd

# Step 1: Load the dataset
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_fb_posts_president_scored_anon.csv"  # Adjust if needed
df = pd.read_csv(file_path)

# Step 2A: Descriptive stats for numeric columns
print("=== Descriptive Stats for Numeric Columns ===")
print(df.describe())

# Step 2B: Descriptive stats for categorical/object columns
print("\n=== Descriptive Stats for Categorical Columns ===")
print(df.describe(include=[object]))

# Step 2C: value_counts and nunique for non-numeric fields
non_numeric_columns = df.select_dtypes(include='object').columns

for col in non_numeric_columns:
    print(f"\n--- {col} ---")
    print("Top 5 Most Frequent Values:")
    print(df[col].value_counts().head(5))
    print(f"Number of Unique Values: {df[col].nunique()}")



import pandas as pd

# Reload the uploaded file
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_tw_posts_president_scored_anon.csv"
df = pd.read_csv(file_path)

# Step 2A: Describe numeric fields
numeric_summary = df.describe(include=[float, int])

# Step 2B: Describe object/categorical fields
categorical_summary = df.describe(include=[object])

# Step 2C: value_counts() and nunique() for non-numeric columns
non_numeric_info = {}
non_numeric_columns = df.select_dtypes(include='object').columns

for col in non_numeric_columns:
    top_values = df[col].value_counts().head(5)
    unique_count = df[col].nunique()
    non_numeric_info[col] = {
        "top_5_value_counts": top_values.to_dict(),
        "n_unique": unique_count
    }

print(numeric_summary)

