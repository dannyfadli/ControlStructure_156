# Program untuk mencetak desain hingga nilai n

# Minta input nilai n dari user
n = int(input("Masukkan nilai n: "))

# Cetak desain hingga nilai n menggunakan loop for
for i in range(1, n + 1):
    
    for j in range(i):  #for j disini untuk mengulangi loop 
        print(i, end=" ")
    print()