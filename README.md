## 1. Was it a challenge to produce identical results?

Yes. Achieving **identical outputs across all three approaches** required careful handling of:

- **Data types**: Pure Python reads everything as strings, unlike `pandas` and `polars`, which infer types.
- **Null handling**: `pandas` automatically skips `NaN` values in numeric summaries; Pure Python does not.
- **Group-by operations**: `pandas.groupby()` is concise; I manually implemented it using `defaultdict` and tuple keys in Python.
- **Precision differences**: Standard deviation calculations may slightly differ due to rounding.

### Solution:
We enforced consistent rules across all approaches:
- Parsed types manually in Python (`try_parse_float`)
- Filtered empty strings explicitly
- Matched column selection and ordering across tools
- Rounded all outputs to 2 decimal places for fair comparison

---

## 2. Do you find one approach easier or more performant?
**Conclusion:** `pandas` is ideal for exploration and visual storytelling. `polars` excels with large-scale pipelines. Pure Python is educational but not scalable.

---

## 3. Coaching a Junior Analyst — What to Recommend?

**Start with `pandas`.** It has:
- Clean syntax
- Strong documentation
- Rapid feedback via `.describe()`, `.groupby()`, `.value_counts()`
- Built-in compatibility with `matplotlib`, `seaborn`, and `Plotly`

---

## 4. Can ChatGPT Help Jump-Start These Approaches?

**Absolutely.** Coding AIs like ChatGPT can:
- Scaffold **template code** for all three strategies
- Suggest null handling, type conversion
- Provide **error diagnostics** and alternative logic paths

---

## 5. 🤔 What Default Approach Do Coding AIs Use?

By default, tools like ChatGPT tend to recommend:

```python
import pandas as pd
df = pd.read_csv("data.csv")
print(df.describe())
