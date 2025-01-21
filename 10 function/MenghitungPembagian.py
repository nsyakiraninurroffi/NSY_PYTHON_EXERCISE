#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung pembagian

def pembagian(a, b):
    if b == 0:
        return "Pembagian dengan nol tidak diperbolehkan!"
    else:
        return a / b


def main():
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    
    hasil = pembagian(a, b)
    print(f"Hasil pembagian: {hasil}")


if __name__ == "__main__":
    main()
