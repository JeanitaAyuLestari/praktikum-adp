pustaka_kita = open("inventaris_buku.txt", "w")
pustaka_kita.close()

with open("inventaris_buku.txt", "a") as file:
    file.write("978-602-40-3210-5, Logika Matematika, Rafi Hidayat, 13, 78000, 100000\n")
    file.write("978-623-55-6677-8, Analisis Data Menggunakan Excel, Irwan Maulana, 17, 58000, 75000\n")
    file.write("978-623-00-4567-8, Statistik untuk Penelitian Sosial, Dr.Budi Santosa, 4, 95000, 120000\n")
    file.write("978-602-01-2345-6, Manajemen Waktu Mahasiswa, Lestari Wulandari, 5, 60000, 75000\n")
    file.write("978-979-88-7766-4, Sistem Informasi Manajemen, Yudi Kurniawan, 10, 92000, 115000\n")
    file.write("978-623-22-3344-9, Teori Belajar dan Pembelajaran, Sulastri Handayani, 7, 90000, 115000\n")
    file.write("978-979-78-5566-4, Literasi Media untuk Pelajar, Andika Surya, 14, 70000, 90000\n")
    file.write("978-602-66-7412-9, Pemasaran Digital, Laila Azzahra, 3, 77000, 100000\n")
    file.write("978-623-44-3322-1, Kepemimpinan dan Organisasi, Desi Lestari, 8, 95000, 120000\n")
    file.write("978-602-33-4433-2, Teknik Menulis Ilmiah, Nina Kusumawardani, 14, 75000, 95000")

file = open("inventaris_buku.txt", "r")
data_buku = []
for baris in file:
    baris_baru = ''
    for huruf in baris:
        if huruf != "\n": #untuk menghilangkan tanda \n
            baris_baru += huruf
    bagian = baris.split(", ") #untuk memisahkan koma dan spasi

    isbn = bagian[0]
    judul = bagian[1]
    penulis = bagian[2]
    stok = int(bagian[3])
    harga_beli = int(bagian[4])
    harga_jual = int(bagian[5])

    buku = {}
    buku["ISBN"] = {'Judul Buku': judul,
                    'Penulis': penulis,
                    'Stok': stok,
                    'Harga Beli': harga_beli,
                    'Harga Jual': harga_jual}
    data_buku.append(buku)
file.close()

for a in data_buku:
    print(a)

total_inventaris = 0
daftar_restock = []
pertama = True

file1 = open("laporan_inventaris.txt", "w")
for buku in data_buku:
    for isbn in buku:
        angka = buku[isbn]
        judul = angka['Judul Buku']
        stok = angka['Stok']
        harga_beli = angka['Harga Beli']
        harga_jual = angka['Harga Jual']

        potensi_keuntungan = stok * (harga_jual - harga_beli)
        nilai_inventaris = stok * harga_beli
        file1.write(judul + " -> Potensi Keuntungan: Rp" + str(potensi_keuntungan) + "\n")

        if pertama:
            keuntungan_tertinggi = potensi_keuntungan
            judul_tertinggi = judul
            keuntungan_terendah = potensi_keuntungan
            judul_terendah = judul
            pertama = False
        else:
            if potensi_keuntungan > keuntungan_tertinggi:
                keuntungan_tertinggi = potensi_keuntungan
                judul_tertinggi = judul
            if potensi_keuntungan < keuntungan_terendah:
                keuntungan_terendah = potensi_keuntungan
                judul_terendah = judul
        total_inventaris = total_inventaris + nilai_inventaris

        if stok < 5:
            daftar_restock.append(judul)

file1.write("\nBuku dengan potensi keuntungan tertinggi:\n")
file1.write(judul_tertinggi + " -> Rp" + str(keuntungan_tertinggi) + "\n")

file1.write("\nBuku dengan potensi keuntungan terendah:\n")
file1.write(judul_terendah + " -> Rp" + str(keuntungan_terendah) + "\n")

file1.write("\nTotal Nilai Inventaris (berdasarkan harga beli): Rp" + str(total_inventaris) + "\n")

file1.write("\nDAFTAR BUKU YANG PERLU RESTOCK (stok < 5):\n")
for buku in daftar_restock:
    file1.write("- " + buku + "\n")

file1.close()