# Program untuk mencetak bilangan ganjil hingga nilai n

# Minta input nilai n dari user
n = int(input("Masukkan nilai n: ")) # n = int dimana input n hanya dapat menerima variable angka dan meminta user untuk measukan nilai

# Cetak bilangan ganjil hingga nilai n menggunakan loop for
for i in range(1, n + 1): 
    if i % 2 != 0: #dalam sesi ini dia mengecek apakah nilai tersebut tdk hbs dibagi 2 jika iya maka print
        print(i, end=" ")