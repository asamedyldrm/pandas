import pandas as pd
import openpyxl

# csv okuma
csv = pd.read_csv("reading_data/ornekcsv.csv", sep=";")
print(csv)

# txt okuma
txt = pd.read_csv("reading_data/duz_metin.txt")
print(txt)
# print(help(pd.read_csv))

print()
df = pd.read_excel("reading_data/ornekx.xlsx")
print(df)
print(type(df))
df.columns = ["A","B","C"]
print(df)