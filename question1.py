import pandas as pd
import json

# read .csv file
df = pd.read_csv(r"C:\Users\user\Desktop\coursework2\cleaned_no_missing_no_outliers.csv")  

columns = ['diet_group', 'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_bio', 'mean_acid']
df_cleaned = df[columns].dropna()

# Group by diet_group and calculate the average for each group.
grouped = df_cleaned.groupby('diet_group').mean().reset_index()
for col in columns[1:]:  # Exclude diet_group itself.
    min_val = grouped[col].min()
    max_val = grouped[col].max()
#Normalization (between 0 and 1)
    grouped[col] = (max_val - grouped[col]) / (max_val - min_val)

# Convert the DataFrame to JSON format 
data = grouped.to_dict(orient='records')

# Save .json
with open(r"C:/Users/user/Desktop/coursework2/radar_data.json", "w") as f:
    json.dump(data, f, indent=2)
