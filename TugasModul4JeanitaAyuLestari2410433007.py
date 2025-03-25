# Pemesanan kursi bioskop
while True: 
    r = int(input("masukan jumlah baris kursi(minimal 4) :"))
    c = int(input("masukan jumlah kolom kursi(minimal 4) :"))
    if r >= 4 or c >= 4:
        break
    else :
        print("upss! Ukuran minimal kursi bioskop adalah 4x4. Silahkan masukan ulang!")
        
jumlah_kursi = r*c
kursi = []
for i in range(jumlah_kursi):
    kursi.append(str(i+1))

while True:
    print("\nLayout Kursi Bioskop:")
    for i in range(r):
        for j in range(c):
            print(f"{kursi[i * c + j]}", end="\t")
        print()

    nomor_kursi = int(input("Pilih nomor kursi yang ingin dipesan(atau 0 untuk selesai) :"))

    if nomor_kursi == 0:
        print("Terimakasih telah memesan tiket bioskop!")
        break
    elif nomor_kursi < 1 or nomor_kursi > jumlah_kursi:
        print("Nomor kursi tidak valid, silahkan memilih kursi yang tersedia!")
    elif kursi[nomor_kursi - 1] == 'X':
        print("kursi sudah dipesan, silahkan pilih kursi yang lain.")
    else:
        kursi[nomor_kursi - 1] = 'X'
        print(f"kursi {nomor_kursi} berhasil dipesan.")