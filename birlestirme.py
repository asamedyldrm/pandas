# Birlestirme (join) Islemleri

import numpy as np
import pandas as pd

a = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(a, columns=["var1", "var2", "var3"])
print(df1)

df2 = df1 + 99
print(df2)

print(pd.concat([df1, df2]))  # index numaraları tekrar ediyor.
print(pd.concat([df1, df2], ignore_index=True))
# print(help(pd.concat))

print(df1.columns)
df2.columns = ["var1","var2","deg3"]
print(df2)
print(df1)
print("-------------")
print(pd.concat([df1,df2], join="inner",ignore_index=True))
# pd.concat([df1,df2], join_axes = [df2.columns])