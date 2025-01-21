# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 21 / 11 / 2024
# Program Menentukan Bilangan Ganjil atau Genap
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


def main():
    angka = int(input("Masukkan angka: "))
    print(f"Angka {angka} adalah {cek_ganjil_genap(angka)}.")


if __name__ == "__main__":
    main()
