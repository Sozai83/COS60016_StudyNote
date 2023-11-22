import pandas as pd
import numpy as np


energy_data = pd.read_csv('./week7csv/energy_data.csv')
season_data = pd.read_csv('./week7csv/season_data.csv')
combined_data = pd.read_csv('./week7csv/combine.csv')


print(energy_data.shape)
print(energy_data.head())
print(energy_data.dtypes)

print(season_data.shape)
print(season_data.head())
print(season_data.dtypes)

print(combined_data.shape)
print(combined_data.head())
print(combined_data.dtypes)

season_data.rename({'max_temp':'maximum_temp',
                            'min_temp': 'minumum_temp'},
                            axis=1,
                            inplace=True)


print(season_data['minumum_temp'].head())


# Determine if there are missing values with the isna().sum() method. 
print(energy_data.isna().sum())
print(season_data.isna().sum())

# View the metadata with the info() method.
print(energy_data.info())


# concat_data = pd.concat([energy_data, season_data])
# print(concat_data)

merged_data = pd.merge(energy_data, season_data, how='inner')
print(merged_data)


merged_data.to_csv('./week7csv/merged_data.csv')