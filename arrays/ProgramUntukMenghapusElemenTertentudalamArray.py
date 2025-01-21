# Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 21 / 11 / 2024
# Program Menghapus Elemen dalam Array


def jumlah_array(arr):
    return sum(arr)


def main():
    n = int(input("Masukkan jumlah elemen dalam array: "))
    arr = []
    
    for i in range(n):
        elemen = float(input(f"Masukkan elemen ke-{i+1}: "))
        arr.append(elemen)
    
    print(f"Jumlah elemen dalam array: {jumlah_array(arr)}")


if __name__ == "__main__":
    main()
