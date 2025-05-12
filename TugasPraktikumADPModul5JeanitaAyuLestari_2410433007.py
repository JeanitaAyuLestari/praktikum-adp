n = int(input("masukkan jumlah mahasiswa praktikum ADP :"))
no = []
nama = []
npre = []
npos = []
nmak = []
nakh = []
for i in range(n):
    print(f"Data mahasiswa ke-{i+1}")
    nama.append(input("Masukkan nama\t\t :"))
    npre.append(float(input("Masukkan nilai pretest\t :")))
    npos.append(float(input("Masukkan nilai postest\t :")))
    nmak.append(float(input("Masukkan nilai makalah\t :")))
    print()

for i in range(n):
    no.append(str(i+1))
    nakh.append(((npre[i])*40/100) + ((npos[i])*40/100) + ((nmak[i])*20/100))
print()
print("="*60)
print("\tNo\tNama\t\t\tNilai Akhir")
print("="*60)
for i in range(n):
    print("\t",no[i],"\t",nama[i],"\t",nakh[i])
    print("_"*60)
print()

for i in range(n):
    jumlah_mahasiswa = len(nakh)
    jumlah_nilai = sum(nakh)
    rata_rata = jumlah_nilai / jumlah_mahasiswa
print(f"Jumlah rata-rata akhir kelas adalah {rata_rata}")
print()

# untuk menentukan nilai tertinggi dan terendah
nilai_tertinggi = nakh[0]
nilai_terendah = nakh[0]
for i in range(len(nakh)):
    if nakh[i] > nilai_tertinggi :
        nilai_tertinggi = nakh[i]
    elif nakh[i] < nilai_terendah :
        nilai_terendah = nakh[i]

# untuk menentukan nama mahasiswa yang mendapatkan nilai tertinggi dan terendah
nama_tertinggi = []
nama_terendah = []
for i in range(len(nakh)):
    if nakh[i] == nilai_tertinggi :
        nama_tertinggi.append(nama[i])
    if nakh[i] == nilai_terendah :
        nama_terendah.append(nama[i])

print("Nilai tertinggi di peroleh oleh :")
for i in range(len(nama_tertinggi)):
    print("Nama\t\t:", nama_tertinggi[i])
    print("Nilai akhir\t:", nilai_tertinggi)
print()

for i in range(len(nama_terendah)):
    print("Nama\t\t:", nama_terendah[i])
    print("Nilai akhir\t:", nilai_terendah)
print()

# Menampilkan data mahasiswa yang nilai akhirnya diatas rata rata kelas
print("Data mahasiswa yang nilai akhir nya diatas rata rata kelas:")
for i in range(len(nakh)):
    if nakh[i] > rata_rata:
        print(f"\nNama\t\t: {nama[i]} \nNilai akhir\t: {nakh[i]}")
        print()