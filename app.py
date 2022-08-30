import pandas as pd

df = pd.read_csv("total_stars.csv")

print(df.columns)
df.drop(['Unnamed: 0'], axis=1, inplace= True)
df.drop(['Unnamed: 6'], axis=1, inplace= True)
df.drop(['Star_Names.1'], axis=1, inplace= True)
df.drop(['Distance.1'], axis=1, inplace= True)
df.drop(['Mass.1'], axis=1, inplace= True)
df.drop(['Radius.1'], axis=1, inplace= True)
print(df.head())

df.reset_index(drop=True, inplace=True)
print(df.head())
print(df.columns)

df = df.dropna()
print(df.dtypes)
print(df.head())

df.to_csv("final_stars.csv")