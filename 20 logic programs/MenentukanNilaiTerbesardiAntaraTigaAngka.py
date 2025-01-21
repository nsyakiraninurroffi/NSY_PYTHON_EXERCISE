#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program Meenentukan nilai terbesar dari tiga angka

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    print(f"Angka terbesar adalah {a}")
elif b >= a and b >= c:
    print(f"Angka terbesar adalah {b}")
else:
    print(f"Angka terbesar adalah {c}")
