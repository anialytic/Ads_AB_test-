import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Ads\\marketing_AB.csv', sep=';')

ad_group_count = df[df['test group']=='ad'].shape[0]
print(ad_group_count)