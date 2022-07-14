# Gozlem ve Degisken Secimi : LOC & ILOC

import numpy as np
import pandas as pd

m = np.random.randint(1,30, size=(10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])
print(df)

# loc : tanimlandigi sekliyle secim yapmak icin kullanilir.

print(df.loc[0:3]) #3'u de dahil eder.

# iloc: alisik oldugumuz indexleme mantigiyla secim yapar.
print("-----------")
# print(df.iloc[0:3])
# print(df.iloc[0,0])
# print(df.iloc[:3,:2])
print(df.loc[0:3,"var3"])
print("-----------")
print(df.iloc[0:3]["var3"])