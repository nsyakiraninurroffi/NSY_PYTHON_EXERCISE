print ("\033[1;35m="*40)
print ("\033[1;31mSUBTOTAL BELANJA")
print ("\033[1;35m="*40)

a1 = int(input("\033[1;33mPensil Rp.2000, Jumlah Pembelian: "))
a2 = int(input("Pulpen Rp.3000, Jumlah Pembelian: "))
a3 = int(input("Penghapus Rp.1000, Jumlah Pembelian: "))
a4 = int(input("Buku Tulis Rp.4000, Jumlah Pembelian: "))
a5 = int(input("Buku Gambar Rp.2000, Jumlah Pembelian: "))

b1 = 2000*a1
b2 = 3000*a2
b3 = 1000*a3
b4 = 4000*a4
b5 = 5000*a5
total = b1+b2+b3+b4+b5
dc = total*12.5/100
hasil = total-dc
print(f'\033[1;34mTotal Belanja Anda : {total}\nTotal Discount 12,5% : {dc}\nTotal Pembayaran Setelah Discount : {hasil}')