import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Ads\\marketing_AB.csv', sep=';', low_memory=False)

ad_group_count = df[df['test group']=='ad'].shape[0]
psa_group_count = df[df['test group']=='psa'].shape[0]

#check rows count
print(ad_group_count)
print(psa_group_count)
print(ad_group_count + psa_group_count)

#count conversion
conv_rate = df.groupby('test group')['converted'].value_counts(normalize=True).unstack()
print(conv_rate)
print('ok')

#delete unimportant columns
df = df[df['test group'].isin(['ad', 'psa'])]

# convert boolean to 1/0
df['converted'] = df['converted'].map({'TRUE': 1, 'FALSE': 0})

#z-test
summary = df.groupby('test group')['converted'].agg(['sum', 'count'])

#print(summary)
#print(summary.shape)

conversions = summary['sum'].to_numpy()
users = summary['count'].to_numpy()

z_stat, p_value = proportions_ztest(conversions, users)
print(f"Z-stat: {z_stat:.3f}, P-value: {p_value:.5f}")
