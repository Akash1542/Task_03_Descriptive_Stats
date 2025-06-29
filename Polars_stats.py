#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import polars as pl

file_path = "Users/namrathaaddala/Downloads/period_03/2024_fb_ads_president_scored_anon.csv"


# ==== Using polars ====
print("\n=== Using polars ===")
df = pl.read_csv(file_path)

# Describe numeric columns
print(df.describe())

# Value counts and unique counts for object (Utf8) columns
for col in df.columns:
    if df[col].dtype == pl.Utf8:
        print(f"\nTop values for {col}:")
        print(df[col].value_counts().sort("counts", descending=True).head(5))
        print(f"Unique count: {df[col].n_unique()}")


import polars as pl

# Step 1: Load the dataset
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_fb_posts_president_scored_anon.csv"
df = pl.read_csv(file_path)

# Step 2A: Use describe() for numeric summary
print("=== Numeric Summary ===")
print(df.describe())

# Step 2B: value_counts() and nunique() for categorical fields
print("\n=== Categorical Value Counts and Unique Counts ===")

# Loop through string/object columns
for col in df.columns:
    if df[col].dtype == pl.Utf8:
        print(f"\n--- {col} ---")
        print("Top 5 Most Frequent Values:")
        print(df[col].value_counts().sort("counts", descending=True).head(5))
        print(f"Number of Unique Values: {df[col].n_unique()}")


import polars as pl

# Step 1: Load dataset
file_path = "2024_tw_posts_president_scored_anon.csv"  # Change path if needed
df = pl.read_csv(file_path)

# Step 2A: Descriptive statistics for numeric columns
print("=== Numeric Summary ===")
print(df.describe())

# Step 2B: Value counts and unique counts for non-numeric fields
print("\n=== Categorical Columns: Top 5 Frequencies and Unique Counts ===")

for col in df.columns:
    if df[col].dtype == pl.Utf8:
        print(f"\n--- {col} ---")
        try:
            value_counts = df[col].value_counts().sort("counts", descending=True).head(5)
            print("Top 5 Most Frequent Values:")
            print(value_counts)
            print("Number of Unique Values:", df[col].n_unique())
        except Exception as e:
            print(f"Error processing column {col}: {e}")
