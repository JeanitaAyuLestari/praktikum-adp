while True:
    baris_a = int(input("masukkan batas baris matriks A: "))
    kolom_a = int(input("masukkan batas kolom matriks A: "))
    baris_b = int(input("masukkan batas baris matriks B: "))
    kolom_b = int(input("masukkan batas kolom matriks B: "))
    if baris_a != kolom_a or baris_b != kolom_b: 
        print("ukuran matriks tidak sama, silahkan input ulang")
    else:
        break

matriksa = []
for i in range(baris_a):
    baris_baru = []
    for j in range(kolom_a):
        baris_baru.append(int(input(f"matriks A[{i}][{j}] : ")))
    matriksa.append(baris_baru)

matriksb = []
for i in range(baris_b):
    baris_baru = []
    for j in range(kolom_b):
        baris_baru.append(int(input(f"matriks B[{i}][{j}] : ")))
    matriksb.append(baris_baru)

print("Matriks A")
for i in range(baris_a):
    for j in range(kolom_a):
        print(matriksa[i][j], end=" ")
    print()
print()

print("Matriks B")
for i in range(baris_b):
    for j in range(kolom_b):
        print(matriksb[i][j], end=' ')
    print()
print()

while True:
    print('Menu Kalkulator Matriks: ')
    print('1. Penjumlahan matriks \n2. Pengurangan matriks \n3. Perkalian matriks \n4. Determinan matriks \n5. Invers matriks \n6. Transpose matriks')
    print()
    pilih = int(input("Pilih menu kalkulator (atau 0 untuk selesai): "))
    if pilih == 0:
        print('Terimakasih telah menggunakan kalkulator matriks ini!')
        break
    elif pilih == 1:
        print("Hasil penjumlahan matriks A dan matriks B")
        hasil = []
        for i in range(baris_a):
            baris_baru = []
            for j in range(kolom_b):
                jumlah = matriksa[i][j] + matriksb[i][j]
                baris_baru.append(jumlah)
            hasil.append(baris_baru)

        for i in range(baris_a):
            for j in range(kolom_b):
                print(hasil[i][j], end=' ')
            print()
        print()
    elif pilih == 2:
        print("Hasil pengurangan matriks A dan matriks B")
        hasil = []
        for i in range(baris_a):
            baris_baru = []
            for j in range(kolom_b):
                jumlah = matriksa[i][j] - matriksb[i][j]
                baris_baru.append(jumlah)
            hasil.append(baris_baru)
        
        for i in range(baris_a):
            for j in range(kolom_b):
                print(hasil[i][j], end=' ')
            print()
        print()
    elif pilih == 3:
        print('Hasil perkalian matriks A dan matriks B')
        hasil = []
        for i in range(baris_a):
            baris_baru = []
            for j in range(kolom_b):
                total = 0
                for k in range(kolom_a):
                    total += matriksa[i][k] * matriksb[k][j]
                baris_baru.append(total)
            hasil.append(baris_baru)

        for i in range(baris_a):
            for j in range(kolom_b):
                print(hasil[i][j], end=' ')
            print()
        print()
    elif pilih == 4:
        if baris_a != kolom_a and baris_b != kolom_b:
            print("tidak bisa mencari determinan matriks, karena ukuran matriks tidak sama, silahkan input matriks nxn")
            break
        else:
            pilihan = int(input("pilih matriks A atau Matriks B untuk mencari determinan (1/2): "))
            if pilihan == 1:
                if baris_a and kolom_a == 2:
                    det2a = matriksa[0][0]*matriksa[1][1] - matriksa[0][1]*matriksa[1][0]
                    print("Determinan dari matriks A adalah", det2a)
                    print()
                elif baris_a and kolom_a == 3:
                    det3a = matriksa[0][0]*((matriksa[1][1]*matriksa[2][2]) - (matriksa[1][2]*matriksa[2][1]) - matriksa[0][1]*((matriksa[1][0]*matriksa[2][2]) - (matriksa[1][2]*matriksa[2][0]) + matriksa[0][2]*((matriksa[1][0]*matriksa[2][1]) - (matriksa[1][1]*matriksa[2][0]))))
                    print()
                    print("Determinan dari matriks A adalah", det3a)
                else:
                    print("tidak bisa mencari determinan matriks A karena ukuran matriks terlalu besar, jadi cari sendiri secara manual")
                    print()
            elif pilihan == 2:
                if baris_b and kolom_b == 2:
                    det2b = matriksb[0][0]*matriksb[1][1] - matriksb[0][1]*matriksb[1][0]
                    print("Determinan dari matriks B adalah", det2b)
                elif baris_b and kolom_b == 3:
                    det3b = matriksb[0][0]*((matriksb[1][1]*matriksb[2][2]) - (matriksb[1][2]*matriksb[2][1]) - matriksb[0][1]*((matriksb[1][0]*matriksb[2][2]) - (matriksb[1][2]*matriksb[2][0]) + matriksb[0][2]*((matriksb[1][0]*matriksb[2][1]) - (matriksb[1][1]*matriksb[2][0]))))
                    print("Determinan dari matriks B adalah", det3b)
                else:
                    print("tidak bisa mencari determinan matriks B karena ukuran matriks terlalu besar, jadi cari sendiri secara manual")
            else:
                print("hanya ada matriks A dan matriks B")
                print()
    elif pilih == 5:
        if baris_a != kolom_a and baris_b != kolom_b:
            print("tidak bisa mencari invers matriks, karena ukuran matriks tidak sama, silahkan input matriks nxn")
            break
        else:
            pilihan = int(input("pilih matriks A atau Matriks B untuk mencari determinan (1/2): "))
            if pilihan == 1:
                if baris_a and kolom_a == 2:
                    det2a = matriksa[0][0]*matriksa[1][1] - matriksa[0][1]*matriksa[1][0]
                    invers2a = [[matriksa[1][1]/det2a, -matriksa[0][1]/det2a], [-matriksa[1][0]/det2a, matriksa[0][0]/det2a]]
                    for i in range(2):
                        for j in range(2):
                            print(f"invers matriks A: \n{invers2a}")
                        print()
                    print()
                elif baris_a and kolom_a == 3:
                    det3a = matriksa[0][0]*((matriksa[1][1]*matriksa[2][2]) - (matriksa[1][2]*matriksa[2][1]) - matriksa[0][1]*((matriksa[1][0]*matriksa[2][2]) - (matriksa[1][2]*matriksa[2][0]) + matriksa[0][2]*((matriksa[1][0]*matriksa[2][1]) - (matriksa[1][1]*matriksa[2][0]))))
                    adj = []
                    for i in range(3):
                        baris_baru = []
                        for j in range(3):
                            baris_baru.append(det3a)
                        adj.append(baris_baru)
                    invers3a = []
                    for i in range(3):
                        baris_baru = []
                        for j in range(3):
                            nilai = adj[i][j]/det3a
                            baris_baru.append(nilai)
                        invers3a.append(baris_baru)

                    print("Invers dari matriks A adalah: ")
                    for i in range(3):
                        for j in range(3):
                            print(f'{invers3a[i][j]}', end=' ')
                        print()
                    print()
                else:
                    print("matriks ukuran A tidak bisa mencari invers karena ukuran matriks tertlalu besar, jadi cari manual saja menggunakan pena dan kertas selembar")
                    print()
            elif pilihan == 2 :
                if baris_b and kolom_b == 2:
                    det2b = matriksb[0][0]*matriksb[1][1] - matriksb[0][1]*matriksb[1][0]
                    invers2b = [[matriksb[1][1]/det2b, -matriksb[0][1]/det2b], [-matriksb[1][0]/det2b, matriksb[0][0]/det2b]]
                    for i in range(2):
                        for j in range(2):
                            print(f"invers matriks B: \n{invers2b}")
                        print()
                    print()
                elif baris_b and kolom_b == 3:
                    det3b = matriksb[0][0]*((matriksb[1][1]*matriksb[2][2]) - (matriksb[1][2]*matriksb[2][1]) - matriksb[0][1]*((matriksb[1][0]*matriksb[2][2]) - (matriksb[1][2]*matriksb[2][0]) + matriksb[0][2]*((matriksb[1][0]*matriksb[2][1]) - (matriksb[1][1]*matriksb[2][0]))))
                    adj = []
                    for i in range(3):
                        baris_baru = []
                        for j in range(3):
                            baris_baru.append(det3b)
                        adj.append(baris_baru)
                    invers3b = []
                    for i in range(3):
                        baris_baru = []
                        for j in range(3):
                            nilai = adj[i][j]/det3b
                            baris_baru.append(nilai)
                        invers3b.append(baris_baru)

                    print("Invers dari matriks B adalah: ")
                    for i in range(3):
                        for j in range(3):
                            print(f'{invers3b[i][j]}', end=' ')
                        print()
                    print()
                else:
                    print("matriks ukuran B tidak bisa mencari invers karena ukuran matriks tertlalu besar, jadi cari manual saja menggunakan pena dan kertas selembar")
                    print()
    elif pilih == 6:
        pilihan = int(input("pilih matriks A atau matriks B (1/2) : "))
        if pilihan == 1:
            print("Transpos dari matriks A :")
            for i in range(baris_a):
                for j in range(kolom_a):
                    print(matriksa[j][i], end=" ")
                print()
            print()
        elif pilihan == 2:
            print("Transpos dari matriks B :")
            for i in range(baris_b):
                for j in range(kolom_b):
                    print(matriksb[j][i], end=" ")
                print()
            print()
        else:
            print("hanya ada matriks A dan matriks B, silahkan pilih ulang")