import pandas as pd
import numpy as np

df = pd.DataFrame({"gruplar": ["A", "B", "C", "A", "B", "C"],
                   "degisken1": [10, 23, 33, 22, 11, 99],
                   "degisken2": [100, 253, 333, 262, 111, 969]})
print(df)

# print(df.apply(np.sum)) #toplamini alir.
# print(df.apply(np.mean))
# gruplar numeric olmadigi icin str'ye yalnizca uygun islemleri yapabiliriz.
print(df.groupby("gruplar").apply(np.sum))
print(df.groupby("gruplar").apply(np.mean))