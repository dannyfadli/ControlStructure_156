#2. Program ini akan menunjukkan angka terbesar dari angka yg diinputkan user
print("Program Angka Terbesar")
angka1=int(input("Masukkan Angka Pertama: "))
angka2=int(input("Masukkan Angka Kedua: "))
angka3=int(input("Masukkan Angka Ketiga: "))
if angka1 >= angka2 and angka1 >= angka3:
    print("Angka", angka1, "merupakan angka terbesar")
elif angka2 >= angka1 and angka2 >= angka3:
    print("Angka", angka2, "adalah angka terbesar")
else:
    print("Angka", angka3, "merupakan angka terbesar")
print('\n')