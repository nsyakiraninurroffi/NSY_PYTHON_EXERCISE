#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 20 / 11 / 2024
# Program Kalkulator Sederhana

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Pembagian dengan nol tidak diperbolehkan."

print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Input dari pengguna
choice = input("Masukkan pilihan (1/2/3/4): ")

num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

if choice == '1':
    print(f"Hasil: {add(num1, num2)}")
elif choice == '2':
    print(f"Hasil: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Hasil: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Hasil: {divide(num1, num2)}")
else:
    print("Pilihan tidak valid.")
