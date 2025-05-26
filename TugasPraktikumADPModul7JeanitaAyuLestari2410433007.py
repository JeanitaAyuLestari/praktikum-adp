def data():
    data_mahasiswa = []
    n = int(input("masukkan jumlah mashasiswa dalam satu kelas : "))
    for i in range(n):
        print(f"Mahasiswa ke-{i+1}")
        nama = input("Nama : ")
        nim = int(input("NIM : "))
        uts = float(input("Nilai UTS : "))
        uas = float(input("Nilai UAS : "))
        tugas = float(input("Nilai Tugas : "))
        nilai_akhir = (uts * 0.35) + (uas * 0.35) + (tugas * 0.35)
        data_mahasiswa.append([nama, nim, uts, uas, tugas, nilai_akhir])
        print()
    return data_mahasiswa

def urutan_data(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][5] < data [j][5]:
                peringkat = data[i]
                data[i] = data[j]
                data[j] = peringkat
    return data

def tampilkan_tabel_data(data):
    print("\nDaftar Nilai Mahasiswa")
    print('~'*95)
    print("|{:<20}|{:<13}|{:<7}|{:<7}|{:<7}|{:<13}|{:<10}|{:<10}|".format('Nama', 'NIM', 'UTS', 'UAS', 'Tugas', 'Nilai akhir', 'Rata-rata', 'Peringkat'))
    print('~'*95)
    uts = 0
    uas = 0
    tugas = 0
    nilai_akhir = 0
    for i in range(len(data)):
        mahasiswa = data[i]
        uts += mahasiswa[2]
        uas += mahasiswa[3]
        tugas += mahasiswa[4]
        nilai_akhir += mahasiswa[5]
        print("|{:<20}|{:<13}|{:<7}|{:<7}|{:<7}|{:<13.2f}|{:<10.2f}|{:<10}|".format(mahasiswa[0], mahasiswa[1], mahasiswa[2], mahasiswa[3], mahasiswa[4], mahasiswa[5], (mahasiswa[2]+mahasiswa[3]+mahasiswa[4])/3, i+1))

    jumlah_data = len(data)
    rata_uts = uts / jumlah_data
    rata_uas = uas / jumlah_data
    rata_tugas = tugas / jumlah_data
    rata_nilai_akhir = nilai_akhir / jumlah_data
    print('~'*95)
    print("|{:<20}|{:<13}|{:<7.2f}|{:<7.2f}|{:<7.2f}|{:<13.2f}|          |          |".format('NILAI RATA-RATA','', rata_uts, rata_uas, rata_tugas, rata_nilai_akhir))
    print('~'*95)

data_mahasiswa = data()
data_mahasiswa = urutan_data(data_mahasiswa)
tampilkan_tabel_data(data_mahasiswa)