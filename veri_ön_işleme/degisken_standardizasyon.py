import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

# Değişken Standardizasyonu

V1 = np.array([1, 3, 6, 5, 7])
V2 = np.array([7, 7, 5, 8, 12])
V3 = np.array([6, 12, 5, 6, 14])

df = pd.DataFrame({
    "V1": V1,
    "V2": V2,
    "V3": V3
})
df = df.astype(float)
print("\n--- Sayısal df ---")
print(df)

# standardizasyon
scaled_df = preprocessing.scale(df)  # kalıcı değildir
print("\n--- Standardizasyon (scale) ---")
print(scaled_df)

# Normalizasyon
normalized_df = preprocessing.normalize(df)
print("\n--- Normalizasyon (normalize) ---")
print(normalized_df)

# Min-Max Dönüşümü
scaler = preprocessing.MinMaxScaler(feature_range=(10, 20))
minmax_df = scaler.fit_transform(df)
print("\n--- Min-Max Dönüşümü (10-20) ---")
print(minmax_df)

# Değişken Dönüşümleri
df = sns.load_dataset('tips')
print("\n--- Tips Veri Seti İlk 5 Satır ---")
print(df.head())

# 0-1 Dönüşümü
lbe = LabelEncoder()
print("\n--- LabelEncoder (sex) İlk 10 Değer ---")
print(lbe.fit_transform(df["sex"])[:10])
df["yeni_sex"] = lbe.fit_transform(df["sex"])
print("\n--- 'yeni_sex' Eklenmiş İlk 5 Satır ---")
print(df[["sex", "yeni_sex"]].head())

# "1 ve Diğerleri(0)" Dönüşümü
df["yeni_day"] = np.where(df["day"].str.contains("Sun", case=False, na=False), 1, 0)
print("\n--- 'yeni_day' (Sun=1, Diğerleri=0) İlk 10 Satır ---")
print(df[["day", "yeni_day"]].head(10))

# Çok Sınıflı Dönüşüm
lbe_day = LabelEncoder()
print("\n--- Çok Sınıflı LabelEncoder (day) İlk 10 Değer ---")
print(lbe_day.fit_transform(df["day"])[:10])

# One Hot Dönüşümü Ve Dummy Değişken Tuzağı
print("\n--- One Hot Öncesi df İlk 5 Satır ---")
print(df.head())
df_one_hot = pd.get_dummies(df, columns=["sex"], prefix=["sex"])
print("\n--- One Hot Dönüşümü Sonrası df_one_hot İlk 5 Satır ---")
print(df_one_hot.head())