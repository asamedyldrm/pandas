import pandas as pd

a = pd.Series([10,20,3,4,5,6])

print(a)
print(type(a))
print(a.axes)
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.values)
print(a.head()) #defaul olarak ilk 5 veriyi veriyor.
print(a.head(3)) #ilk 3 veriyi veriyor.
print(a.tail(3)) #son 3 veriyi veriyor.

# index isimlendirmesi

seri = pd.Series([99,32,450,85,6], index=[1,3,5,7,9])
print(seri)

seri = pd.Series([99,32,450,85,6], index=["a","b","c","d","e"])
print(seri)
print(seri["a"])
print(seri["a":"c"])

# sozluk uzerinden liste olusturmak

sozluk = {"reg":10,"log":11,"cart":12}
seri = pd.Series(sozluk)
print(seri)

# iki seri birlestirerek seri olusturma

print(pd.concat([seri,seri]))
