import os
import time
from termcolor import colored, cprint

cprint("=====SELAMAT DATANG DI PERMAINAN PUKUL TIKUS=====", 'red', 'on_blue')
nama = input("Daftarkan nama anda : ")
print()

print('Terimakasih telah mendaftar permainan ini!')
time.sleep(2)
os.system('cls')

print('Cara bermain: \nSilahkan input cepat angka 1-9 untuk memukul tikus')
time.sleep(3)
print('Jika kamu telat, maka tikus akan kabur')
time.sleep(2)
os.system('cls')

print('Bersiap!')
time.sleep(2)
os.system('cls')

print('Permainan akan segera di mulai')
time.sleep(2)
os.system('cls')

print('Dalam hitungan')
time.sleep(2)
os.system('cls')

for i in range(3, 0, -1):
    os.system('cls')
    print(i)
    time.sleep(1)
os.system('cls')

score = 0
ronde = 1
max_ronde = 10

while ronde <= max_ronde:
    for i in range(1):
        posisi_tikus = ((ronde * 3 + score * 2 + i * 4) % 9) + 1
        os.system('cls')
        cprint(f"Ronde {ronde} | Skor:{score}\n", 'blue', 'on_yellow')

        papan_tikus = [] 
        nomor = 1
        for i in range(3):
            baris = []
            for j in range(3):
                if nomor == posisi_tikus:
                    cprint("[🐭 ]", 'yellow', 'on_red', end=" ")
                    baris.append("🐭")
                else:
                    cprint(f"[ {nomor} ]", 'yellow', 'on_red', end=" ")
                    baris.append(str(nomor))
                nomor += 1
            papan_tikus.append(baris)
            print()

        mulai = time.time()
        jawaban = input("->>")
        selesai = time.time()

        durasi = selesai - mulai
        
        if durasi > 1.5:
            print("Telat! Tikus nya kabur! Ayo lebih cepat lagi")
        elif jawaban.isdigit():
            if int(jawaban) == posisi_tikus:
                print("Tikus terpukul!")
                score+=1
            else:
                print("Yahh kamu salah pukul")
        else:
            print("Tidak ada dalam rentang")

        ronde+=1
        time.sleep(1)

os.system('cls')
print("Waktu habis!")
time.sleep(2)
os.system('cls')
print("Permainan Selesai!")
time.sleep(2)
os.system('cls')

def tampilan_score():
    cprint("=====SCORE AKHIR=====", 'red', 'on_blue')
    print(f"{nama} kamu mendapatkan score {score}")
    print()
    cprint("TERIMAKASIH TELAH BERMAIN", 'green')

data = tampilan_score()

data_pemain = {nama : score}
with open("data_score.txt", "a") as file:
    for nama, score in data_pemain.items():
        file.write(f"{nama}: {score}\n")

print()
cprint('Data telah tersimpan di data_score.txt', 'red')