# Tebak Angka BUUM! 
# Misalkan Batas Angka Positif = n
# Misalkan Angka BUUM! = k

# Pemain 1
# Tentukan batas angka positif 
# Tentukan angka BUUM
print("SELAMAT DATANG DIPERMAINAN TEBAK ANGKA BOM \nAnda diminta untuk memilih salah satu angka \nBermainlah bersama pasangan atau teman anda agar lebih SERU! \nSELAMAT BERMAIN \nSEMOGA KEMENANGAN ADA DI TANGAN ANDA")
print("=====PEMAIN 1=====")
n = 25
k = "BUUM!"
i = 1
print("\nderetan angka kematian :")
for i in range(1, n+1) :
    if i % 6 == 0 :
        print(k, end="  ")
    else :
        print(i, end="  ")
print("\n==================")

# Pemain 2
# Jika angka yang dipilih adalah angka BUUM, maka kamu kalah
# Jika angka yang dipilih adalah bukan angka BUUM, maka kamu menang
print("=====PEMAIN 2=====")
n = int(input("Pilih salah satu angka kelipatan :"))
i = 1
while i <= n+1 :
    if n % 6 == 0 :
        print(f"{n} adalah angka kelipatan 6, YAHH KAMU KALAH!:(")
        break
    elif n>=25 :
        print("Pilihan tidak terpenuhi, silahkan ulangi kembali") 
        break
    else :
        print(f"{n} bukan angka kelipatan 6, horeeyyy kamu menanggggggg")
        break
print("==================")
print("Permainan sudah berakhir \nTerimakasih sudah main di permainan ini \nJangan lupa mampir ke sini lagi untuk bermain")