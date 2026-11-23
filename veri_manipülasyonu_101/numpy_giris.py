import numpy as np

# Numpy Array'i Oluşturmak.
a = np.array([1, 2, 3, 4])
print("\n--- Tek Boyutlu Array 'a' ---")
print(a)
print("Tipi:", type(a))

print("\n--- int Tipine Dönüştürülmüş Array ---")
print(np.array([1.23, 2, 3, 4], dtype="int"))

# Sıfırdan Array Oluşturmak.
print("\n--- Sıfırlardan Oluşan Array (zeros) ---")
print(np.zeros(10, dtype=int))

print("\n--- Birlerden Oluşan (3x5) Array (ones) ---")
print(np.ones((3, 5), dtype=int))

print("\n--- 5'lerden Oluşan (3x5) Array (full) ---")
print(np.full((3, 5), 5))

print("\n--- Linspace (0-2 arası 3 parça) ---")
print(np.linspace(0, 2, 3))

print("\n--- Arange (0-100 arası 4'er artan) ---")
print(np.arange(0, 100, 4))

print("\n--- Normal Dağılımlı (3x3) Array ---")
print(np.random.normal(10, 4, (3, 3)))

print("\n--- Rastgele Tam Sayı (2x2) Array ---")
print(np.random.randint(0, 23, (2, 2)))

# NumPy Array Özellikleri.
b = np.random.randint(10, size=(3, 6))
print("\n--- 'b' Array ve Özellikleri ---")
print(b)
print("Boyut sayısı (ndim), Şekil (shape), Eleman sayısı (size), Veri tipi (dtype):")
print(b.ndim, b.shape, b.size, b.dtype)

# Reshaping
x = np.arange(1, 10)
print("\n--- Reshaping (3x3) ---")
print(x.reshape(3, 3))

# Concatenation
u = np.array([3, 4, 5, 6])
y = np.array([7, 8, 9, 0])
print("\n--- Tek Boyutta Concatenation ---")
print("x ve y birleşimi:", np.concatenate([x, y]))
print("u ve y birleşimi:", np.concatenate([u, y]))

# İki Boyutta Concatenation
v = np.array([[1, 2, 3], [4, 5, 6]])
print("\n--- İki Boyutlu 'v' Array ---")
print(v)
print("\nSatır bazında birleştirme (axis=0):\n", np.concatenate([v, v]))  # satır bazında birşeltirir.
print("\nSütun bazında birleştirme (axis=1):\n", np.concatenate([v, v], axis=1))  # Sütun bazında birleştirir

# Splitting
e = np.array([1, 2, 3, 4, 12, 13, 14, 15, 21, 22])
print("\n--- Tek Boyutta Splitting ([4, 7]) ---")
print("e dizisi:", e)
print("Bölünmüş parçalar:", np.split(e, [4, 7]))
# Her bölümü ayrı array yapmak için
h, j, k = np.split(e, [4, 7])
print("h:", h, "| j:", j, "| k:", k)

# İki Boyutta Splitting
m = np.arange(16).reshape(4, 4)
print("\n--- İki Boyutlu 'm' Array (4x4) ---")
print(m)
print("\nYatay bölme (vsplit - [2]):\n", np.vsplit(m, [2]))
ust, alt = np.vsplit(m, [2])  # vsplit ile yatayda böleriz.
print("üst:\n", ust)
print("alt:\n", alt)

m = np.arange(16).reshape(4, 4)
print("\nDikey bölme (hsplit - [2]):\n", np.hsplit(m, [2]))
sag, sol = np.hsplit(m, [2])  # hsplit ile dikeyde böleriz.
print("sağ:\n", sag)
print("sol:\n", sol)

# Sorting
v = np.array([2, 1, 4, 3, 5])
print("\n--- Tek Boyutta Sıralama (Sorting) ---")
print("np.sort(v) çıktısı:", np.sort(v))  # Burada veri setinin orijinal yapısını bozmaz.
print("np.sort sonrası v:", v)

v.sort()  # Burada veri setinin orijinal yapısını bozar.
print("v.sort() sonrası v:", v)

# İki Boyutta Sorting
m = np.random.normal(20, 5, (3, 3))
print("\n--- İki Boyutlu 'm' Array (Sıralama Öncesi) ---")
print(m)

print("\nSatıra göre sıralama (axis=1):\n", np.sort(m, axis=1))  # Satıra sırlamaa yapar.

print("\nSütuna göre sıralama (axis=0):\n", np.sort(m, axis=0))  # Sütuna göre sıralama yapar.