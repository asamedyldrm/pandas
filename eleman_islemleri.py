# Eleman Islemleri

import numpy as np
import pandas as pd

a = np.array([1,2,3,4,5])
seri = pd.Series(a)
print(seri)
print(seri[0])
print(seri[0:3])

seri = pd.Series([120,200,350,560], index=["reg","loj","cart","rf"])
print(seri)
print(seri.index)
print(seri.keys)
print(list(seri.items()))
print(seri.values)

# elaman sorgulama

print("reg" in seri)
print(seri["reg"])

# fansy eleman

print(seri[["rf","reg"]])

seri["reg"] = 999
print(seri["reg"])
print(seri)

print(seri["reg":"cart"])