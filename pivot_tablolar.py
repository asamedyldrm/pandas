import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.head())

print(titanic.groupby("sex")["survived"].mean()) #titanic hayatta kalma durumunu cinsiyete gore siraliyor.
print(titanic.groupby("sex")[["survived"]].mean())
print(titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack())
print(titanic.groupby(["sex","class"])[["survived"]].mean().unstack())

# pivot ile table - daha kolay kismi

print(titanic.pivot_table("survived", index = "sex", columns="class"))

print(titanic.age.head())

age = pd.cut(titanic.age, [0,18,90])
print(age.head(10))
print(titanic.pivot_table("survived", ["sex", age], "class"))