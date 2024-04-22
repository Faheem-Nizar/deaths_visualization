import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('physicians-per-1000-people.csv')

# Display the first few rows of the DataFrame
print(df.head())
grouped = df.groupby('Code')
arrays = {}

# Iterate over groups
for group_id, group_data in grouped:
    # Extract values from the group and store in array
    arrays[group_id] = group_data.iloc[:].values

df_new = pd.DataFrame(columns=['Code', 'Year', 'Physicians (per 1,000 people)'])

# Display arrays
for group_id, array in arrays.items():
    years, data = array[:, 2], array[:, 3]
    new_yrs, new_data = [], []
    slope, finyr, findat = 0, 0, 0
    for ind in range(len(years) - 1):
        y1, y2, d1, d2 = years[ind], years[ind+1], data[ind], data[ind+1]
        new_yrs.append(y1)
        new_data.append(d1)
        slope = (d2 - d1)/(y2-y1)
        finyr, findat = y2, d2
        for j in range(y1+1, y2):
            new_yrs.append(j)
            new_data.append((d2 - d1)/(y2-y1)*(j-y1) + d1)
            
        # new_yrs.append(y2)
        # new_data.append(d2)
    for yr in range(finyr, 2020):
        new_yrs.append(yr)
        new_data.append(slope*(yr-finyr) + findat)
    for j in range(len(new_yrs)):
        if(new_yrs[j] < 1990):
            continue
        new_row = {'Code': group_id, 'Year': new_yrs[j], 'Physicians (per 1,000 people)': new_data[j]}
        # Append the new row to the DataFrame
        df_new = df_new.append(new_row, ignore_index=True)
    
    # print(years, data, new_cols)
    # break
print(df_new.head())

df_new.to_csv('physicians-per-1000-people-modified.csv', index=False)