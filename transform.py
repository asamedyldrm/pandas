import pandas as pd

df = pd.DataFrame({"gruplar": ["A", "B", "C", "A", "B", "C"],
                   "degisken1": [10, 23, 33, 22, 11, 99],
                   "degisken2": [100, 253, 333, 262, 111, 969]})

print(df)
# print(df*9)
# print(df["degisken1"]*9)

# kendi tanimladigimiz bir fonksiyonu degiskenler uzerinde gezdirmek icin.

# df_a = df.iloc[:,1:3] #gruplar verileri numeric olmadigi icin ya boyle ya da diger turlu ayirabiliriz.

print(df[["degisken1","degisken2"]].transform(lambda x:(x-x.mean()) / x.std()))

# lambda kisminda verdigimiz islemi istedigimiz degiskenler uzerinde islem yapar.
# yakaladigi tum verilerden verilerin ortalamasini cikartip standart sapmaya boler.