import pandas as pd
import seaborn as sns

df = pd.DataFrame({"gruplar": ["A","B","C","A","B","C"],
                   "veri": [10,11,52,23,43,55]}, columns= ["gruplar","veri"])

print(df)

gruplama_toplulastirma = df.groupby("gruplar").mean()
print(gruplama_toplulastirma)

df = sns.load_dataset("planets")
print(df.head())

print(df.groupby("method")["orbital_period"].describe())