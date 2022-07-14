import pandas as pd
import numpy as np

df = pd.DataFrame({"gruplar": ["A", "B", "C", "A", "B", "C"],
                   "degisken1": [10, 23, 33, 22, 11, 99],
                   "degisken2": [100, 253, 333, 262, 111, 969]})

print(df)

# kendi kisisel fonksiyonlarimizi bir filtreleme araci olarak degiskenler uzerinde sorgulamak icin FILTER!

def filter_func(x):
    return x["degisken1"].std() > 9
# standart sapmasi 9'dan buyuk olanlari sirala demek icin bu sekilde bir kullanim uyguluyoruz.
print(df.groupby("gruplar").std())
print(df.groupby("gruplar").filter(filter_func))
