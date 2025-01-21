#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Program Menghitung Nilai Prima

def cek_bilangan_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True


def main():
    angka = int(input("Masukkan angka: "))
    
    if cek_bilangan_prima(angka):
        print(f"{angka} adalah bilangan prima.")
    else:
        print(f"{angka} bukan bilangan prima.")


if __name__ == "__main__":
    main()
