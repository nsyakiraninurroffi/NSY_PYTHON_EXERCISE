#ibuat oleh : Nesya Kirani Nurroffi
# Tanggal Pengerjaan : 26 / 10 / 2024
# Program KOnversi Suhu

def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    pilihan = input("Pilih konversi (1: Celsius ke Fahrenheit, 2: Fahrenheit ke Celsius): ")
    
    if pilihan == "1":
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = celsius_ke_fahrenheit(celsius)
        print(f"{celsius}° Celsius = {fahrenheit}° Fahrenheit")
    elif pilihan == "2":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celsius = fahrenheit_ke_celsius(fahrenheit)
        print(f"{fahrenheit}° Fahrenheit = {celsius}° Celsius")
    else:
        print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
