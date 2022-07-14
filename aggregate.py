# Ileri Toplulastirma Islemleri (Aggregate, filter, transform, apply)

import pandas as pd
import numpy as np

df = pd.DataFrame({"gruplar": ["A", "B", "C", "A", "B", "C"],
                   "degisken1": [10, 23, 33, 22, 11, 99],
                   "degisken2": [100, 253, 333, 262, 111, 969]})

# Aggregate

print(df.groupby("gruplar").aggregate(["min", np.median, max]))
# dısaridan bir veri getirdigimiz icin tirnak kullanmadik! numpy'dan aldigimiz icin.
# pandas'in icindeki fonksiyonlari tirnak icine aliyoruz.


# farkli degiskenler icin farkli istatiksel veri almak icin:
print(df.groupby("gruplar").aggregate({"degisken1":"min","degisken2":"max"}))
