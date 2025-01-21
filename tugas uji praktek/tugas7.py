print ("\033[1;35m============================")
print ("\033[1;33mCek Discount")
print ("\033[1;35m============================")
total_belanja = int(input('\033[1;37mMasukkan total Belanja Anda: '))

if total_belanja >= 100000:
    print ("\033[1;31mSelamat Anda Mendapatkan Discount :) ")
    
elif total_belanja < 100000:
    print ('\033[1;34mMaaf Anda Tidak Mendapatkan Discount\nBelanja Lebih Dari "100K" Untuk Mendapatkan Discount')
    