import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.neighbors import LocalOutlierFactor

# Aykırı Değer Yakalamak

df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna()
print("\n--- Veri Seti İlk 5 Satır ---")
print(df.head())

df_table = df["table"]
print("\n--- 'table' Değişkeni İlk 5 Satır ---")
print(df_table.head())

sns.boxplot(x=df_table)
plt.title("table Değişkeni Boxplot")
plt.show()

Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3 - Q1

# Eşik değer hesaplama
alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR
print(f"\nAlt Sınır: {alt_sinir:.2f} | Üst Sınır: {ust_sinir:.2f}")

aykiri_tf = (df_table < alt_sinir) | (df_table > ust_sinir)
print("\n--- Alt Sınırın Altındaki Aykırı Değerler ---")
alt_aykiri_tf = df_table < alt_sinir
print(alt_aykiri_tf.head())
print(df_table[alt_aykiri_tf])

# Aykırı Değeri Problemini Çözmek

# Silme
print("\n--- Silme İşlemi ---")
print("df_table tipi:", type(df_table))
df_table_df = pd.DataFrame(df_table)
t_df = df_table_df[~((df_table_df < alt_sinir) | (df_table_df > ust_sinir)).any(axis=1)]
print("Silme sonrası boyut:", t_df.shape)

# Ortalama ile doldurma
print("\n--- Ortalama ile Doldurma ---")
df_ortalama = df["table"].copy()
ortalama_deger = df_ortalama.mean()
df_ortalama[aykiri_tf] = ortalama_deger
print(f"Atanan ortalama değer: {ortalama_deger:.2f}")
print(df_ortalama[aykiri_tf].head())

# Baskılama Yöntemi
print("\n--- Baskılama Yöntemi ---")
df_baskilama = df["table"].copy()
df_baskilama[df_baskilama < alt_sinir] = alt_sinir
df_baskilama[df_baskilama > ust_sinir] = ust_sinir
print("Baskılama sonrası min/max:", df_baskilama.min(), df_baskilama.max())

# Çok Değişkenli Aykırı Gözlem Analizi
# Local Outlier Factor (LOF)
print("\n--- Çok Değişkenli Aykırı Gözlem Analizi (LOF) ---")
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
clf.fit_predict(df)
df_scores = clf.negative_outlier_factor_

print("İlk 10 LOF skoru:", df_scores[0:10])
print("En düşük 20 LOF skoru:", np.sort(df_scores)[0:20])
print("14. sıradaki LOF skoru:", np.sort(df_scores)[13])

esik_deger = np.sort(df_scores)[13]
aykiri_tf = df_scores > esik_deger

yeni_df = df[df_scores > esik_deger]
print("\n--- Aykırı Olmayan Gözlemler ---")
print(yeni_df)  # Aykırı olmayan gözlemler

print("\n--- Aykırı Gözlemler ---")
print(df[df_scores < esik_deger])  # Aykırı gözlemler