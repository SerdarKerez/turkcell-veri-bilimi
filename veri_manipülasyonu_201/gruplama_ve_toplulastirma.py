import pandas as pd
import seaborn as sns
import numpy as np

#Basit Toplulaştırma Fonksiyonları
df = sns.load_dataset("planets")
print(df.head())
print(df.shape)

df["mass"].mean()                   #Mass değişken için ortalama hesaplar
df["mass"].count()                  #Mass değerlerini sayar
df["mass"].min()                    #Mass değişkeninin en küçük değerini döndürür.
df["mass"].sum()                    #toplar


#Gruplama işlemleri
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'veri': [10, 11, 52, 23, 43, 55]}, columns=['gruplar', 'veri'])
print(df)

df.groupby("gruplar")               #Gruplama nesnesi oluşturur; tek başına çıktı üretmez.
df.groupby("gruplar").mean(numeric_only=True)  #Gruplara göre sayısal ortalamayı alır.
df.groupby("gruplar").sum(numeric_only=True)   #Gruplara göre toplamı alır.

#Aggregate
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10, 23, 33, 22, 11, 99],
                   'degisken2': [100, 253, 333, 262, 111, 969]},
                  columns=['gruplar', 'degisken1', 'degisken2'])
print(df)

print(df.groupby("gruplar").aggregate(["min", "median", "max"]))  #Gruplara birden fazla toplulaştırma fonksiyonu uygular.

#Filter
def filter_func(x):
    return x["degisken1"].std() > 9
print(df.groupby("gruplar").filter(filter_func))  #filter_func() değil, fonksiyon referansı (filter_func) verilir; koşulu sağlayan grupları tutar.


#Transform
df_a = df.iloc[:, 1:3]
print(df_a.transform(lambda x: x - x.mean()))  #Orijinal boyut korunarak her elemana grup/sütun bazlı dönüşüm uygular.


#Apply
print(df.apply(np.sum))             #Tüm sütunlara/satırlara fonksiyon uygular (metin içeren 'gruplar' sütununu birleştirir).

print(df.groupby("gruplar").apply(lambda g: g.mean(numeric_only=True), include_groups=False))  #Gruplara özel fonksiyon çalıştırır; sayısal sütun ortalamasını alır.


#Pivot Tablolar
titanic = sns.load_dataset('titanic')
print(titanic.head())

print(titanic.groupby("sex")[["survived"]].mean())  #Cinsiyete göre hayatta kalma ortalaması.
print(titanic.groupby(["sex", "class"], observed=False)[["survived"]].aggregate("mean").unstack())  #"survive" -> "survived", ".aggrate" -> ".aggregate("mean")` düzeltildi.

#Pivot ile Table
print(titanic.pivot_table("survived", index="sex", columns="class", observed=False))  #Satır ve sütun kırılımıyla özet pivot tablo oluşturur.