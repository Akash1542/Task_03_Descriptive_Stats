import csv
import math
from collections import defaultdict, Counter
from typing import List, Dict, Any, Tuple

# Load the CSV file
def load_csv(filepath: str) -> Tuple[List[str], List[Dict[str, Any]]]:
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        headers = reader.fieldnames
    return headers, rows

# Convert to float if possible
def try_parse_float(value: str) -> Any:
    try:
        return float(value)
    except ValueError:
        return value.strip()

# Compute stats for a column
def compute_stats(values: List[Any]) -> Dict[str, Any]:
    numeric_values = [v for v in values if isinstance(v, float)]
    non_numeric_values = [v for v in values if not isinstance(v, float)]
    
    stats = {'count': len(values)}
    
    if numeric_values:
        stats['mean'] = sum(numeric_values) / len(numeric_values)
        stats['min'] = min(numeric_values)
        stats['max'] = max(numeric_values)
        if len(numeric_values) > 1:
            mean = stats['mean']
            variance = sum((x - mean) ** 2 for x in numeric_values) / (len(numeric_values) - 1)
            stats['stddev'] = math.sqrt(variance)
    
    if non_numeric_values:
        counter = Counter(non_numeric_values)
        stats['unique'] = len(counter)
        stats['most_common'] = counter.most_common(1)[0]
    
    return stats

# Analyze all columns in the dataset
def analyze_dataset(headers: List[str], rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    columns = defaultdict(list)
    for row in rows:
        for h in headers:
            value = try_parse_float(row[h])
            columns[h].append(value)
    
    summary = {}
    for col, values in columns.items():
        summary[col] = compute_stats(values)
    return summary

# Group by one or more columns
def group_by(rows: List[Dict[str, Any]], keys: List[str]) -> Dict[Tuple, List[Dict[str, Any]]]:
    grouped = defaultdict(list)
    for row in rows:
        key = tuple(row[k] for k in keys)
        grouped[key].append(row)
    return grouped

# Analyze grouped data
def analyze_groups(headers: List[str], rows: List[Dict[str, Any]], group_keys: List[str]) -> Dict:
    grouped_data = group_by(rows, group_keys)
    group_summaries = {}
    for group, group_rows in grouped_data.items():
        group_summary = analyze_dataset(headers, group_rows)
        group_summaries[group] = group_summary
    return group_summaries

# ======= Usage Example =======

if __name__ == "__main__":
    file_path = "/Users/namrathaaddala/Downloads/period_03/2024_fb_ads_president_scored_anon.csv"  # Change path as needed
    headers, rows = load_csv(file_path)

    # Overall analysis
    overall_stats = analyze_dataset(headers, rows)

    # Group by 'page_id'
    grouped_by_page = analyze_groups(headers, rows, ['page_id'])

    # Group by 'page_id' and 'ad_id'
    grouped_by_page_ad = analyze_groups(headers, rows, ['page_id', 'ad_id'])

    # Print a sample of the results
    print("=== Overall Stats ===")
    for col, stats in overall_stats.items():
        print(f"{col}: {stats}")

    print("\n=== Sample Grouped by page_id ===")
    for key, summary in list(grouped_by_page.items())[:2]:  # Only show first 2 groups
        print(f"\nGroup: {key}")
        for col, stats in summary.items():
            print(f"  {col}: {stats}")




from typing import List, Dict, Any, Tuple
import json

# Load CSV using standard library
def load_csv(filepath: str) -> Tuple[List[str], List[Dict[str, Any]]]:
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        headers = reader.fieldnames
    return headers, rows

# Try converting to float
def try_parse_float(value: str) -> Any:
    try:
        return float(value)
    except ValueError:
        return value.strip()

# Compute stats for a column
def compute_stats(values: List[Any]) -> Dict[str, Any]:
    numeric = [v for v in values if isinstance(v, float)]
    non_numeric = [v for v in values if not isinstance(v, float)]
    
    stats = {'count': len(values)}
    
    if numeric:
        stats['mean'] = sum(numeric) / len(numeric)
        stats['min'] = min(numeric)
        stats['max'] = max(numeric)
        if len(numeric) > 1:
            variance = sum((x - stats['mean']) ** 2 for x in numeric) / (len(numeric) - 1)
            stats['stddev'] = math.sqrt(variance)
    
    if non_numeric:
        counter = Counter(non_numeric)
        stats['unique'] = len(counter)
        stats['most_common'] = counter.most_common(1)[0]
    
    return stats

# Analyze the full dataset
def analyze_dataset(headers: List[str], rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    columns = defaultdict(list)
    for row in rows:
        for h in headers:
            value = try_parse_float(row[h])
            columns[h].append(value)
    return {col: compute_stats(values) for col, values in columns.items()}

# Group rows by one or more keys
def group_by(rows: List[Dict[str, Any]], keys: List[str]) -> Dict[Tuple, List[Dict[str, Any]]]:
    grouped = defaultdict(list)
    for row in rows:
        key = tuple(row[k] for k in keys)
        grouped[key].append(row)
    return grouped

# Analyze stats within each group
def analyze_groups(headers: List[str], rows: List[Dict[str, Any]], group_keys: List[str]) -> Dict:
    grouped = group_by(rows, group_keys)
    return {group: analyze_dataset(headers, rows) for group, rows in grouped.items()}

# Convert tuple keys to strings for JSON output
def stringify_keys(d: Dict[Tuple, Any]) -> Dict[str, Any]:
    return {str(k): v for k, v in d.items()}

# Main function
def main():
    file_path = "/Users/namrathaaddala/Downloads/period_03/2024_fb_posts_president_scored_anon.csv"  # Update if needed
    headers, rows = load_csv(file_path)

    overall_stats = analyze_dataset(headers, rows)
    grouped_by_page = analyze_groups(headers, rows, ["Facebook_Id"])
    grouped_by_page_post = analyze_groups(headers, rows, ["Facebook_Id", "post_id"])

    # Save summary to JSON
    output = {
        "overall": overall_stats,
        "grouped_by_Facebook_Id": stringify_keys({k: grouped_by_page[k] for k in list(grouped_by_page)[:2]}),
        "grouped_by_Facebook_Id_post": stringify_keys({k: grouped_by_page_post[k] for k in list(grouped_by_page_post)[:2]})
    }

    with open("summary_output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print("Analysis complete. Results saved to summary_output.json")

if __name__ == "__main__":
    main()


from typing import List, Dict, Any, Tuple
import json

# Step 1: Load the dataset using only the standard library
def load_csv(filepath: str) -> Tuple[List[str], List[Dict[str, Any]]]:
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        headers = reader.fieldnames
    return headers, rows

# Helper to convert string to float when possible
def try_parse_float(value: str) -> Any:
    try:
        return float(value)
    except ValueError:
        return value.strip()

# Step 2: Compute stats for a column
def compute_stats(values: List[Any]) -> Dict[str, Any]:
    numeric_values = [v for v in values if isinstance(v, float)]
    non_numeric_values = [v for v in values if not isinstance(v, float)]
    
    stats = {'count': len(values)}
    
    if numeric_values:
        stats['mean'] = sum(numeric_values) / len(numeric_values)
        stats['min'] = min(numeric_values)
        stats['max'] = max(numeric_values)
        if len(numeric_values) > 1:
            mean = stats['mean']
            variance = sum((x - mean) ** 2 for x in numeric_values) / (len(numeric_values) - 1)
            stats['stddev'] = math.sqrt(variance)
    
    if non_numeric_values:
        counter = Counter(non_numeric_values)
        stats['unique'] = len(counter)
        stats['most_common'] = counter.most_common(1)[0]
    
    return stats

# Analyze the dataset column-wise
def analyze_dataset(headers: List[str], rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    columns = defaultdict(list)
    for row in rows:
        for h in headers:
            value = try_parse_float(row[h])
            columns[h].append(value)
    
    summary = {}
    for col, values in columns.items():
        summary[col] = compute_stats(values)
    return summary

# Step 3: Group rows by one or more keys
def group_by(rows: List[Dict[str, Any]], keys: List[str]) -> Dict[Tuple, List[Dict[str, Any]]]:
    grouped = defaultdict(list)
    for row in rows:
        try:
            key = tuple(row[k] for k in keys)
            grouped[key].append(row)
        except KeyError:
            continue
    return grouped

# Analyze each group separately
def analyze_groups(headers: List[str], rows: List[Dict[str, Any]], group_keys: List[str]) -> Dict:
    grouped_data = group_by(rows, group_keys)
    group_summaries = {}
    for group, group_rows in grouped_data.items():
        group_summary = analyze_dataset(headers, group_rows)
        group_summaries[group] = group_summary
    return group_summaries

# Load and run analysis on the uploaded file
file_path = "/Users/namrathaaddala/Downloads/period_03/2024_tw_posts_president_scored_anon.csv"
headers, rows = load_csv(file_path)

# Dataset-wide stats
overall_stats = analyze_dataset(headers, rows)

# Determine valid column names for grouping
group_keys_page = "page_id" if "page_id" in headers else headers[0]
group_keys_ad = "ad_id" if "ad_id" in headers else headers[1]

# Grouped by "page_id"
grouped_by_page_id = analyze_groups(headers, rows, [group_keys_page])

# Grouped by ("page_id", "ad_id")
grouped_by_page_ad = analyze_groups(headers, rows, [group_keys_page, group_keys_ad])

# Prepare sample output (truncated for preview)
sample_output = {
    "overall": {k: v for k, v in list(overall_stats.items())[:5]},  # First 5 columns
    "grouped_by_page_id_sample": {str(k): grouped_by_page_id[k] for k in list(grouped_by_page_id)[:2]},
    "grouped_by_page_ad_sample": {str(k): grouped_by_page_ad[k] for k in list(grouped_by_page_ad)[:2]}
}

# Show output preview
json.dumps(sample_output, indent=2)[:1500]
