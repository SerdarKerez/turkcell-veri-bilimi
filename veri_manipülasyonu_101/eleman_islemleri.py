import numpy as np

# Index İle Elemanlara Erişmek
a = np.random.randint(10, size=10)
print("\n--- Tek Boyutlu Dizi 'a' ---")
print(a)
print("İlk ve son eleman:", a[0], a[-1])
a[0] = 21  # Elemanı değiştirebiliriz.
print("a[0]=21 sonrası 'a':", a)

# İki boyutta elemanlara erişmek
b = np.random.randint(10, size=(3, 6))
print("\n--- İki Boyutlu Dizi 'b' ---")
print(b)
print("b[0,0] değeri:", b[0, 0])
b[0, 0] = 21
print("b[0,0]=21 sonrası 'b':\n", b)

# Array Alt Kümesine Erişmek
c = np.arange(20, 50)
print("\n--- 'c' Dizisi (20-49) ---")
print(c)
print("İlk 3 eleman (c[0:3]):", c[0:3])
print("1'den başlayarak 2'şer atlayarak (c[1::2]):", c[1::2])

# İki boyutta slice işlemleri
d = np.random.randint(10, size=(5, 5))
print("\n--- İki Boyutlu Dizi 'd' ---")
print(d)
print("\nİlk sütun (d[:,0]):", d[:, 0])  # Sütun seçer
print("İlk satır (d[0,:]):", d[0, :])  # Satır seçer
print("Alt blok (d[0:2, 0:3]):\n", d[0:2, 0:3])  # Hem satır hem sütun seçer

# Alt Küme Üzerinde İşlem Yapmak
e = np.random.randint(10, size=(5, 6))
alt_e = e[0:3, 0:2]
print("\n--- 'e' Dizisi ---")
print(e)
print("\nAlt küme 'alt_e' (e[0:3, 0:2]):\n", alt_e)

# Fancy Index ile Elemanlara Erişmek
v = np.arange(0, 30, 3)
al_getir = [1, 3, 4, 5]
print("\n--- Fancy Index (v[al_getir]) ---")
print("v dizisi:", v)
print("Seçilen indeksler [1, 3, 4, 5]:", v[al_getir])

# Koşullu Eleman İşlemleri
n = np.array([1, 2, 3, 4, 5])
print("\n--- Koşullu Eleman İşlemleri ('n') ---")
print(n < 3)  # Her değeri kontrol eder.
print("3'ten küçük elemanlar:", n[n < 3])