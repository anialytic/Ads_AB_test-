import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Ads\\marketing_AB.csv', sep=';', low_memory=False)

ad_group_count = df[df['test group']=='ad'].shape[0]
psa_group_count = df[df['test group']=='psa'].shape[0]

#check rows count
print(ad_group_count)
print(psa_group_count)
print(ad_group_count + psa_group_count)

#count conversion
conv_rate = (
    df.groupby('test group')['converted']
      .value_counts(normalize=True)
      .unstack()
)
print(conv_rate)
