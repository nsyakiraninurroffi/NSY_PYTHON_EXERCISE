def soal1():
    print(f'''{'*'*42}
            PROGRAM PYTHON
        OLEH : NESYA KIRANI NURROFFI
            KELAS : PPLG 2
{'*'*42}''')

def soal2():
    print('Hello')
    print(3.14)
    print(14)
    
def soal3():
    QTY = 23
    harga_sepatu = 45000
    print(f'hasil = {QTY*harga_sepatu}')
    
def soal4():
    nama_barang = 'Kertas'
    jumlah_barang = 20
    harga = 1000000
    ketersediaan = True

    print(f'''Nama Barang : {nama_barang}
    Jumlah Barang : {jumlah_barang}
    Harga Barang : {harga}
    Ketersediaan : {str(ketersediaan).lower()}''')
    
def soal5():
    angka1 = 87.77
    angka2 = 66.50
    angka3 = 97.5

    t12 = angka1+angka2
    r12 = t12 / 2

    print(f'''Jumlah Dari Ketiga Angka Tersebut Adalah : {t12}
    Dengan Rata - Rata : {r12}''')
    
while True:
    userInput = int(input(
        "pilih rumus yang akan dipakai: \n\n1.Soal 1\n2.Soal 2\n3.Soal 3\n4.Soal 4\n5.Soal 5\n\n0.keluar dari program\n\npilih nomor berapa: "))
    if(userInput == 1):
        soal1()
    elif(userInput == 2):
        soal2()
    elif(userInput == 3):
        soal3()
    elif(userInput == 4):
        soal4()
    elif(userInput == 5):
        soal5()
    else:
        break