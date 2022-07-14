# Kosullu Eleman Islemleri

import numpy as np
import pandas as pd

m = np.random.randint(1,30, size=(10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])
print(df)

print(df["var1"])
print(df["var1"][0:2])
print(df[0:2][["var1","var2"]])

print(df[df.var1>20])
print(df[df.var1>20]["var2"])

print(df[(df.var1>20) & (df.var3<25)])
print(df.loc[(df.var1>15), ["var1","var2"]]) #degisken secme bilgisi de gondermek icin loc ifadesini gireriz.
print(df.loc[df.var1>15][["var1","var2"]]) #su sekilde de degisken secebiliriz.
