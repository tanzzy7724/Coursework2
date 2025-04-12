import pandas as pd
import json

df = pd.read_csv(r"C:\Users\user\Desktop\coursework2\cleaned_no_missing_no_outliers.csv")

# Calculate the average indicators for each age group.
columns = ['age_group', 'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_bio', 'mean_acid']
df_cleaned = df[columns].dropna()
grouped = df_cleaned.groupby('age_group').mean().reset_index()

# Normalization (between 0 and 1)
for col in columns[1:]:
    min_val = grouped[col].min()
    max_val = grouped[col].max()
    grouped[col] = (grouped[col] - min_val) / (max_val - min_val)

# Convert to JSON format.
result = grouped.to_dict(orient="records")

# Save .json
with open("age_radar_data.json", "w") as f:
    json.dump(result, f, indent=2)
