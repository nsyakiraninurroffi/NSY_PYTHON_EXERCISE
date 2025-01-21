#  Dibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 08 / 11 / 2024
# soal 10 Berat badan ideal ada hubungannya dengan tinggi badan seseorang.
# Untuk menentukan berat badan ideal, tinggi badan dikurangi 100, 
# lalu dikurangi lagi dengan 10% dari hasil pengurangan pertama. 
# Tulislah algoritma yang membaca tinggi badan lalu menentukan berat badan yang ideal untuk tinggi tersebut.

def hitung_berat_badan_ideal(tinggi_badan):
    hasil_pertama = tinggi_badan - 100
    pengurangan_10_persen = hasil_pertama * 0.1
    berat_ideal = hasil_pertama - pengurangan_10_persen
    return berat_ideal

tinggi = float(input("Masukkan tinggi badan Anda (cm): "))
berat_ideal = hitung_berat_badan_ideal(tinggi)

print(f"Berat badan ideal untuk tinggi {tinggi} cm adalah {berat_ideal:.2f} kg.")