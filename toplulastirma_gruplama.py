# Toplulastirma ve Gruplama (Aggregation & Grouping)

# Basit toplulastirma fonksiyonlari
# -count()
# -first()
# -last()
# -mean()
# -median()
# -min()
# -max()
# -std()
# -var()
# -sum()

import seaborn as sns

df = sns.load_dataset("planets")
print(df.head())
print(df.shape)
# print(df.mean()) #genel ortalama
print(df["mass"].mean()) #mass isimli degiskenin ortalamasi
print(df["mass"].count())
print(df["mass"].min()) #min deger
print(df["mass"].max()) #max deger
print(df["mass"].sum()) #degiskenleri toplar
print(df["mass"].std()) #standart sapma
print(df["mass"].var()) #varyans
print(df.describe()) #onemli dataframeleri betimlemek, tanimlamak icin kullanilir.
print(df.describe().T) #transpozunu almak
print(df.dropna().describe().T) #eksik gozlemleri silerek verir.