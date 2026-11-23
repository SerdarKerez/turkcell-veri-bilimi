import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns

# Eksik Veri Analizi

# Hızlı Çözüm

V1 = np.array([1, 3, 6, np.nan, 7, 1, np.nan, 9, 15])
V2 = np.array([7, np.nan, 5, 8, 12, np.nan, np.nan, 2, 3])
V3 = np.array([np.nan, 12, 5, 6, 14, 7, np.nan, 2, 31])

df = pd.DataFrame({
    "V1": V1,
    "V2": V2,
    "V3": V3
})

print("\n--- df Tablosu ---")
print(df)
print("\nEksik değer sayıları:\n", df.isnull().sum())  # Eksik değerlerin sayısını verir.
print("\nDolu değer sayıları:\n", df.notnull().sum())  # Dolu değerlerin sayısını verir.
print("\nToplam eksik değer sayısı:", df.isnull().sum().sum())  # Toplam eksik değer sayısını verir.

print("\n--- Eksik Değer Maskesi (df.isnull()) ---")
print(df.isnull())
print("\n--- Eksik Değer Olan Satırlar ---")
print(df[df.isnull().any(axis=1)])  # eksik değer olan satırları getirir.
print("\n--- Tamamı Dolu Olan Satırlar ---")
print(df[df.notnull().all(axis=1)])  # Dolu olanları getirir.

# Eksik Değerlerin Silinmesi

print("\n--- dropna() Sonucu ---")
print(df.dropna())  # Kalıcı değil.
# df.dropna(inplace=True)  # Kalıcıdır.

# Basit Değer Atama

# df["V1"].fillna(df["V1"].mean())  # Ortalamasıyla doldurur.
# df["V1"].fillna(0)  # 0 ile doldurur.

df_ortalama_atama = df.apply(lambda x: x.fillna(x.mean()), axis=0)  # Her bir eksikliği o değişkenin kendi ortalamasıyla doldurur.
print("\n--- Sütun Ortalamalarıyla Doldurulmuş df ---")
print(df_ortalama_atama)

# Eksik Veri Yapısının Görselleştirilmesi
msno.bar(df)
plt.show()

msno.matrix(df)
plt.show()

dd = sns.load_dataset('planets')
print("\n--- Planets Veri Seti İlk 5 Satır ---")
print(dd.head())

msno.matrix(dd)
plt.show()

msno.heatmap(dd)  # Isı haritası
plt.show()

# Silme Yöntemleri
V1 = np.array([1, 3, 6, np.nan, 7, 1, np.nan, 9, 15])
V2 = np.array([7, np.nan, 5, 8, 12, np.nan, np.nan, 2, 3])
V3 = np.array([np.nan, 12, 5, 6, 14, 7, np.nan, 2, 31])

dc = pd.DataFrame({
    "V1": V1,
    "V2": V2,
    "V3": V3
})

print("\n--- dc Tablosu ---")
print(dc)
print("\nTüm değerleri eksik satırlar silinince (how='all'):\n", dc.dropna(how="all"))
print("\nEksik içeren sütunlar silinince (axis=1):\n", dc.dropna(axis=1))
print("\nTamamı eksik sütunlar silinince (axis=1, how='all'):\n", dc.dropna(axis=1, how="all"))

# Basit Değer Atama Yöntemleri

# Sayısal değişkenlerde atama
print("\n--- df.fillna(df.mean()[:]) ---")
print(df.fillna(df.mean()[:]))
print("\n--- df.fillna(df.mean()['V1':'V2']) ---")
print(df.fillna(df.mean()["V1":"V2"]))
print("\n--- V3 Medyan ile Doldurma ---")
print(df["V3"].fillna(df["V3"].median()))
print("\n--- df.where ile Ortalama Atama ---")
print(df.where(pd.notna(df), df.mean(), axis="columns"))

# Kategorik Değişken Kırılımında Değer Atama

V1 = np.array([1, 3, 6, np.nan, 7, 1, np.nan, 9, 15])
V2 = np.array([7, np.nan, 5, 8, 12, np.nan, np.nan, 2, 3])
V3 = np.array([np.nan, 12, 5, 6, 14, 7, np.nan, 2, 31])
V4 = np.array(["IT", "IT", "IK", "IK", "IK", "IK", "IK", "IT", "IT"])

dy = pd.DataFrame({
    "maas": V1,
    "V2": V2,
    "V3": V3,
    "departman": V4
})
print("\n--- dy Tablosu ---")
print(dy)
print("\n--- Departman Bazında Maaş Ortalamaları ---")
print(dy.groupby("departman")["maas"].mean())
print("\n--- Departman Kırılımında Maaş Ataması ---")
print(dy["maas"].fillna(dy.groupby("departman")["maas"].transform("mean")))

# Kategorik Değişkenlerde Değer Atama
V1 = np.array([1, 3, 6, np.nan, 7, 1, np.nan, 9, 15])
V4 = np.array(["IT", np.nan, "IK", "IK", "IK", "IK", "IK", "IT", "IT"], dtype=object)

dk = pd.DataFrame({
    "maas": V1,
    "departman": V4
})
print("\n--- dk Tablosu ---")
print(dk)
print("\n--- Kategorik Değişken Mod ile Doldurma ---")
print(dk["departman"].fillna(dk["departman"].mode()[0]))

# Tahmine Dayalı Değer Atama Yöntemleri
from ycimpute.imputer import knnimput

df_titanic = sns.load_dataset('titanic')
df_titanic = df_titanic.select_dtypes(include=['float64', 'int64'])

print("\n--- Titanic Sayısal Sütunlar İlk 5 Satır ---")
print(df_titanic.head())
print("\n--- Titanic Eksik Değer Sayıları (Önce) ---")
print(df_titanic.isnull().sum())

var_names = list(df_titanic)
n_df = np.array(df_titanic)
dff = knnimput.KNN(k=4).complete(n_df)
dff = pd.DataFrame(dff, columns=var_names)

print("\n--- KNN Sonrası Eksik Değer Sayıları ---")
print(dff.isnull().sum())