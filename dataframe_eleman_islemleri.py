# Eleman Islemleri

import numpy as np
import pandas as pd

s1 = np.random.randint(10, size=5)
s2 = np.random.randint(10, size=5)
s3 = np.random.randint(10, size=5)

sozluk = {"var1": s1, "var2": s2, "var3": s3}
print(sozluk)

df = pd.DataFrame(sozluk)
print(df)

print(df[0:1])
print(df.index)
df.index = ["a", "b", "c", "d", "e"]
print(df)
print(df["c":"e"])

# Silme

print(df.drop("a", axis=0))
print(df)

df.drop("a", axis=0, inplace=True)  # DataFrame uzerindeki degisikligin kalici olmasini saglar!
print(df)

# fancy

l = ["c", "e"]
print(df.drop(l, axis=0))
# print(df)

print("var1" in df)

l = ["var1", "var4", "var2"]

for i in l:
    print(i in df)

print(df)

df["var4"] = df["var1"] / df["var3"]
print(df)

df.drop("var4", axis=1, inplace=True)
print(df)

# fancy

l = ["var1", "var2"]
print(df.drop(l, axis=1))
