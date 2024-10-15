# Minta input nilai n dari user
n = int(input("Masukkan nilai n: "))

# Inisialisasi nilai a dan b untuk deret Fibonacci
a, b = 0, 1

# Cetak deret Fibonacci hingga nilai n
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b