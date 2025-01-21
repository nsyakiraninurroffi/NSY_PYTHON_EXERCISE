#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# Tuliskan algoritma yang membaca panjang sebuah benda dalam satuan meter,
# lalu mengonversinya ke dalam satuan
# inchi, kaki, dan yard (1 inchi = 25.4 mm, 1 kaki = 30.48 cm, dan 1 yard = 0.9144 m).

def konversi_panjang(panjang_meter):
    inchi = panjang_meter * 39.3701
    kaki = panjang_meter * 3.28084
    yard = panjang_meter * 1.09361
    return inchi, kaki, yard

panjang = float(input("Masukkan panjang benda (meter): "))
inchi, kaki, yard = konversi_panjang(panjang)

print(f"Panjang dalam inchi: {inchi:.2f}")
print(f"Panjang dalam kaki: {kaki:.2f}")
print(f"Panjang dalam yard: {yard:.2f}")