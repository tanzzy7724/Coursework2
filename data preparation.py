import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read .csv file
df = pd.read_csv(r"C:\Users\user\Desktop\coursework2\Results_21Mar2022.csv")
print("Original number of rows：", df.shape[0])

# Delete missing data
columns_to_check = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_bio', 'mean_acid']
df_cleaned = df.dropna(subset=columns_to_check)
print(" Row count after removing missing values：", df_cleaned.shape[0])

# Detect and remove outliers.
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df_filtered = df[(df[column] >= lower) & (df[column] <= upper)]
    print(f"name{column}，{df.shape[0] - df_filtered.shape[0]} outliers were removed")
    return df_filtered

# Outliers were handled column by column based on the data with missing values already removed.
for col in columns_to_check:
    df_cleaned = remove_outliers_iqr(df_cleaned, col)

# save completed data
df_cleaned.to_csv("cleaned_no_missing_no_outliers.csv", index=False)
print(" The cleaned data has been saved as：cleaned_no_missing_no_outliers.csv")
