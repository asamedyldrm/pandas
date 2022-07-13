# Pandas DataFrame Olusturma
import pandas as pd
import numpy as np

l = [1, 2, 39, 67, 90]
m = np.arange(1, 10).reshape(3, 3)

# DataFrame'ler veri bilimi ve yapay zeka alaninda cok kullanilir.

df = pd.DataFrame(m, columns=["var1", "var2", "var3"])
print(df)

# df isimlendirme

df = pd.DataFrame(m, columns=["var1", "var2", "var3"])
print(df.head())
df.columns = ["deg1", "deg2", "deg3"]
print(df.columns)
print(df)

print(df.axes)  # satir ve sutun bilgilerini veriyor.
print(df.shape)
print(df.ndim)
print(df.size)
print(df.values)  # numpy nesnesine yani ndarray nesnesine ceviriyor.
print(type(df.values))
print(df.head())
print(df.tail(1))

# numpy ile dataframe olusturma

a = np.array([1, 2, 3, 4, 5])
df = pd.DataFrame(a, columns=["deg1"])
