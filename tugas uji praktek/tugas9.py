b = int(input("Masukkan panjang benda dengan satuan m: "))

I_MM = 1000/25.4
K_MM = 100/30.48
Y_MM = 0.9144

i = int(I_MM*b)
k = int(K_MM*b)
y = int(Y_MM*b)

print(f'{b} m, ini berarti panjang suattu benda\n{y} "INCHI +" {k} "KAKI +"" {i} "YARD"')