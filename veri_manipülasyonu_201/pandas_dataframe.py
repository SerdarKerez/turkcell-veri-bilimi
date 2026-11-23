import pandas as pd
import numpy as np

#Pandas Dataframe Oluşturma/İsimlendirme
L = [1,2,3,4,5]
df_liste = pd.DataFrame(L, columns = ["degisken_ismi"])  #Oluşan DataFrame'i değişkene atadık.
print(L)

m = np.arange(1,10).reshape((3,3))
df_matris = pd.DataFrame(m, columns = ["var1","var2","var3"])
print(m)

#Df isimlendirme
df = pd.DataFrame(m, columns = ["var1","var2","var3"])
print(df.head())
df.columns = ("deg1","deg2","deg3")
print(df)

df.axes                             #Satır ve Sütun bilgisi verir. ("Sartır" yazım hatası düzeltildi.)
df.shape                            #boyut bilgisini verir (satır, sütun sayısı)
df.ndim                             #kaç boyutlu olduğunu söyler
df.size                             #Toplam eleman sayısını verir. (İçerik değil, adet döndürür.)
df.values                           #Değerleri çekip numpy arrayine dönüştürerek sunar


#Pandas Dataframe Eleman İşlemleri
s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

sozluk = {"var1":s1,"var2":s2,"var3":s3}
print(sozluk)
dd = pd.DataFrame(sozluk)
print(dd)

#Silme
dd.drop(2,axis = 0)                 #Kalıcı değildir,İnplace komutu ile kalıcı hale getirilir.


#Fancy ile silme
L = ["c","e"]
dd.drop(L, axis = 0, errors="ignore")  #dd'nin indeksi 0-4 arası olduğu için "c","e" varsa siler, yoksa hata vermez.

#Değişken silmek
dd.drop("var2", axis = 1, inplace = True)

#Gözlem ve değişken Seçimi:loc & iloc

m = np.random.randint(1,30, size = (10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])
print(df)

#loc (Tanımlandığı şekil ile seçim yapmak için kullanılır.)
print(df.loc[0:3])


#iloc (Alışık olduğumuz indeksleme mantığı ile seçim yapar.)
print(df.iloc[0:3])


#Koşullu Eleman işlemleri
print(df[df.var1 > 15])
print(df[df.var1 > 15]["var1"])
print(df[(df.var1 > 15) & (df.var3 < 5)])               #İki koşulun her birini parantez içine alıp df[...] içinde filtreledik.
print(df.loc[df.var1 > 15, ["var1","var2"]])            #loc içinde satır ve sütun ayrımı virgülle yapılır; loc olmazsa da çift parantez gerekir.
print(df[df.var1 > 15][["var1","var2"]])

#Birleştirme (Join) İşlemleri
n = np.random.randint(1,30, size = (5,3))
df1 = pd.DataFrame(n, columns = ["var1","var2","var3"])
print(df1)
df2 = df1 + 99
print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],ignore_index = True))

pd.concat([df1,df2],join = "inner")                 #Kesişimlerine göre birleştirir.

pd.concat([df1,df2], axis=1).reindex(columns=df1.columns)  #Eski join_axes parametresi kaldırıldığı için güncel karşılığı eklendi.


#İleri Birleştirme İşlemleri
#Birebir birleştirme
df3 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'],
                    'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'İK']})
print(df3)

df4 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'],
                    'ilk_giris': [2010, 2009, 2014, 2019]})
print(df4)

pd.merge(df3,df4)                           #Birebir birleştirir.
pd.merge(df3,df4, on = "calisanlar")        #Sütun adındaki "çalisanlar" -> "calisanlar" yazım hatası düzeltildi.

#Çoktan teke
df5 = pd.merge(df3,df4)
df6 = pd.DataFrame({'grup': ['Muhasebe', 'Muhendislik', 'İK'],
                    'mudur': ['Caner', 'Mustafa', 'Berkcan']})

print(pd.merge(df5,df6))