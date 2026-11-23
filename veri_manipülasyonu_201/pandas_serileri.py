import pandas as pd
import numpy as np

#Pandas Serileri Oluşturmak
seri = pd.Series([1,2,3,4,5])              #Değerleri indexleriyle beraber tutar.
seri.axes                                  #İndex bilgilerine erişiriz.
seri.dtype                                 #Veri tipini döndürür.
seri.size                                  #Eleman sayısını döndürür.
seri.ndim                                  #Boyut bilgisini döndürür.
seri.values                                #NumPy daki gibi sadece değer bilgisine erişiriz.
seri.head(3)                               #ilk 3 değeri getirir
seri.tail(3)                               #Sondan 3 değeri getirir.

#index isimlendirilmesi
pd.Series([123,141,151,161], index = [1,2,3,4])
seri1 = pd.Series([123,141,151,161], index = ["a","b","c","d"])
print(seri1["a":"c"])                      #Etiket dilimlemede bitiş ("c") dahildir.

#Sözlük üzerinden Liste oluşturmak
sozluk = pd.Series({"reg":10, "log":11,"cart":12})
print(sozluk)

#İki Seriyi Birleştirme
print("------------------------------")
cseri = pd.concat([seri,seri1,sozluk])
print(cseri)

#Serilerde Eleman İşlemleri
a = np.array([1,2,3,4,5])
seri3 = pd.Series(a)                       #pd.series yerine pd.Series olmalı.
print(type(a))

x = pd.Series([131,121,111,101], index = ["reg","loj","cart","rf"])  #pd.Series düzeltildi.
print(x.index)                             #x.keys metot olduğu için x.index + x.keys TypeError verir.
print(list(x.items()))

#Eleman Sorgulama
print("reg" in x)                          #İndeks etiketleri arasında "reg" var mı kontrol eder.

#Fancy İndex Yaklaşımı
print(x[["rf","reg"]])                     #İstenen sırayla birden fazla indeksi seçer.