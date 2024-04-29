import pandas as pd
file_path = '/Users/trevorgladstone/Downloads/PS_2024.04.28_22.19.16.csv'
data = pd.read_csv(file_path)
print("Original Data:")
print(data)
missing_values = data.isnull().sum()
print("\nMissing Values:")
print(missing_values)
cleaned_data = data.dropna()
cleaned_data.reset_index(drop=True, inplace=True)
print("\nCleaned Data:")
print(cleaned_data)
cleaned_data.to_csv('cleaned_data.csv', index=False)

import numpy as np
import matplotlib.pyplot as plt
required_columns = ['pl_orbsmax', 'pl_rade', 'st_rad', 'st_lum']
cleaned_data = data.dropna(subset=required_columns)

synth_data = pd.DataFrame()
pl_orbsmax: np.random.uniform(0, 5, size=len(cleaned_data))
pl_rade: np.random.uniform(0, 10, size=len(cleaned_data))
st_rad: np.random.uniform(0.1, 100, size=len(cleaned_data))
st_lum: np.random.uniform(0.1, 1000, size=len(cleaned_data))

def habitable_zone(pl_orbsmax, st_rad, st_lum):
    inner_radius = np.sqrt(st_lum)
    outer_radius = np.sqrt(st_lum / 0.53)
    return (pl_orbsmax >= inner_radius) & (pl_orbsmax <= outer_radius)
cleaned_data['habitable_zone'] = habitable_zone(cleaned_data['pl_orbsmax'], cleaned_data['st_rad'], cleaned_data['st_lum'])
plt.figure(figsize=(8, 6))
plt.scatter(cleaned_data['st_rad'], cleaned_data['st_lum'], c=cleaned_data['habitable_zone'], cmap='coolwarm', alpha=0.5)
plt.xlabel('Stellar Luminosity')
plt.ylabel('Planet Distance')
plt.title('Habitable Zone Distribution')
plt.colorbar(label='Habitable Zone')
plt.grid(True)
plt.show()
