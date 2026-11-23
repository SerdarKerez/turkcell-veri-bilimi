import numpy as np

# ufunc
a = np.array([1, 2, 3, 4, 5, 6])
print("\n--- ufunc İşlemleri ('a' Dizisi) ---")
print("a - 1:", np.subtract(a, 1))  # Her elemandan 1 çıkarır.
print("a + 1:", np.add(a, 1))  # Her elemana 1 ekler.
print("a * 3:", np.multiply(a, 3))  # Her Elemanı 3 ile çarpar.
print("a / 2:", np.divide(a, 2))  # Her elemanı 2 ye böler.

print("\n--- Mutlak Değer (np.absolute) ---")
print(np.absolute(np.array([-3])))  # Mutlak değerini alır.
# Bunlar gibi fonksiyonları cheatsheetlerden bulabiliriz.

# Numpy ile İki Bilinmeyenli Denklem Çözümü

# 5 * x0 + x1 = 12
# x0 + 3 * x1 = 10
x = np.array([[5, 1], [1, 3]])
y = np.array([12, 10])
z = np.linalg.solve(x, y)
print("\n--- İki Bilinmeyenli Denklem Çözümü [x0, x1] ---")
print(z)