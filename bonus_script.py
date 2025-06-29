
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_tw_posts_president_scored_anon.csv"
df = pd.read_csv(file_path)

# Set plot style
sns.set(style="whitegrid")

# Select relevant numeric columns
numeric_cols = ['likeCount', 'retweetCount', 'replyCount', 'quoteCount', 'viewCount']
numeric_cols = [col for col in numeric_cols if col in df.columns]

# Create Histograms
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], bins=50, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Create Boxplots
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Create bar plot for top authors if available
if 'author_id' in df.columns:
    plt.figure(figsize=(10, 6))
    top_authors = df['author_id'].value_counts().head(10)
    sns.barplot(x=top_authors.values, y=top_authors.index, palette="viridis")
    plt.title("Top 10 Most Active Authors")
    plt.xlabel("Number of Tweets")
    plt.ylabel("Author ID")
    plt.tight_layout()
    plt.show()



# Load the newly uploaded Facebook dataset
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_tw_posts_president_scored_anon.csv"
df = pd.read_csv(file_path)

# Use whitegrid style for clarity
sns.set(style="whitegrid")

# Identify numeric columns for plotting
numeric_cols = ['Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care', 'Post Views']
numeric_cols = [col for col in numeric_cols if col in df.columns]

# Create Histograms
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], bins=50, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Create Boxplots
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Create a bar plot for top Page Categories if available
if 'Page Category' in df.columns:
    plt.figure(figsize=(10, 5))
    top_categories = df['Page Category'].value_counts().head(10)
    sns.barplot(x=top_categories.values, y=top_categories.index, palette="Set2")
    plt.title("Top 10 Page Categories")
    plt.xlabel("Number of Posts")
    plt.ylabel("Page Category")
    plt.tight_layout()
    plt.show()



# Load the Facebook Ads dataset
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_fb_ads_president_scored_anon.csv"
df = pd.read_csv(file_path)

# Set seaborn style
sns.set(style="whitegrid")

# Identify numeric columns that are likely to be relevant
numeric_cols = ['spend', 'impressions', 'Overperforming Score']
numeric_cols = [col for col in numeric_cols if col in df.columns]

# Plot histograms
for col in numeric_cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], bins=40, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Plot boxplots to show spread and outliers
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Create bar plot for top sponsors if available
if 'Sponsor Name' in df.columns:
    top_sponsors = df['Sponsor Name'].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_sponsors.values, y=top_sponsors.index, palette="Set2")
    plt.title("Top 10 Sponsors by Ad Count")
    plt.xlabel("Number of Ads")
    plt.ylabel("Sponsor Name")
    plt.tight_layout()
    plt.show()
