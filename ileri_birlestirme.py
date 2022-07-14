import pandas as pd

# birebir birlestirme (pd.merge)

df1 = pd.DataFrame({"calisanlar": ["Ali", "Ayse", "Veli", "Fatma"],
                    "grup": ["Muhasebe", "Muhendislik", "Muhendislik", "IK"]})

df2 = pd.DataFrame({"calisanlar": ["Ali", "Ayse", "Veli", "Fatma"],
                    "ilk_giris": [2010, 2009, 2014, 2019]})

print(df1)
print(df2)

birlestir = pd.merge(df1, df2) #birebir birlestirme komutu
print(birlestir)
pd.merge(df1,df2, on="calisanlar") #bu sekilde de ozel olarak belirtebiliriz.

# coktan teke

df3 = pd.merge(df1,df2)
print(df3)

df4 = pd.DataFrame({"grup": ["Muhasebe","Muhendislik","IK"],
                    "mudur": ["Caner", "Mustafa","Berkcan"]})
print(df4)

birlestir2 = pd.merge(df3,df4)
print(birlestir2)

# coktan coka

df5 = pd.DataFrame({"grup": ["Muhasebe","Muhasebe","Muhendislik","Muhendislik","IK","IK"],
                    "yetenekler": ["matematik","excel","kodlama","linux","excel","yonetim"]})
print(df5)
print(df1)

print(pd.merge(df1,df5))
