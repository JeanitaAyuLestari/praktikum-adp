# Data Maskapai dan Harga Tiket
print("=====================================DATA MASKAPAI====================================")
print("| Kode Maskapai | Tujuan Maskapai | Kelas Ekonomi | Kelas Bisnis | Kelas First Class |")
print("|      3012     | Padang-Jakarta  | Rp. 800.000   | Rp. 850.000  | Rp. 900.000       |")
print("|      4015     | Padang-Batam    | Rp. 500.000   | Rp. 550.000  | Rp. 700.000       |")
print("|      4050     | Padang-Bandung  | Rp. 700.000   | Rp. 750.000  | Rp. 850.000       |")
print("======================================================================================")

# Data Diri
print("==========DATA DIRI==========")
nama = input("Nama Pembeli :")
umur = int(input("Umur Pembeli :"))
jenis_kelamin = input("Jenis Kelamin Pembeli :")
print(".............................")

# Memilih Kode Maskapai
print("==========KODE MASKAPAI==========")
print("1. 3012 - Padang - Jakarta")
print("2. 4015 - Padang - Batam")
print("3. 4050 - Padang - Bandung")
print(".................................")
kode = input("Pilih kode maskapai yang anda inginkan (3012/4015/4050) :")

# Menu Jenis Maskapai
if kode == "3012" : 
    tujuan = "Padang - Jakarta"
    harga_ekonomi = 800000
    harga_bisnis = 850000
    harga_first_class = 900000
elif kode == "4015" :
    tujuan = "Padang - Batam"
    harga_ekonomi = 500000
    harga_bisnis = 550000
    harga_first_class = 700000
elif kode == "4050" :
    tujuan = "Padang - Bandung"
    harga_ekonomi = 700000
    harga_bisnis = 750000
    harga_first_class = 850000
else :
    print("Kode Maskapai Tidak Berlaku")

# Memilih Tujuan Maskapai Anda
print(f"\nAnda memilih maskapai dengan tujuan : {tujuan}")
print("...........................................")

# Kelas Penerbangan
print("==========PILIH KELAS PENERBANGAN==========")
print(f"1. Ekonomi - Rp {harga_ekonomi:,}")
print(f"2. Bisnis - Rp {harga_bisnis:,}")
print(f"3. Fisrt Class - Rp {harga_first_class:,}")
print("...........................................")
#Pilih Kelas Penerbangan Sesuai Budget (kalau tidak ada budget tidak perlu naik pesawat naik angkot aja wkwkwkwkwkwk)
kelas = input("Pilih kelas sesuai budget anda (Ekonomi/Bisnis/First Class):")

# Menentukan Harga Tiket Pesawat Sesuai Kelas
if kelas.lower () == "ekonomi" :
    harga_tiket = harga_ekonomi 
elif kelas.lower () == "bisnis" :
    harga_tiket = harga_bisnis
elif kelas.lower () == "first class" :
    harga_tiket = harga_first_class 
else :
    print("Kelas yang anda pilih tidak berlaku")

jumlah_tiket = int(input("Jumlah tiket yang anda beli :"))

# Menghitung Harga Total dan Diskon Sebesar 20% 
total_harga = harga_tiket * jumlah_tiket 
if jumlah_tiket > 3 :
    diskon = 0.2 * total_harga
    total_harga -= diskon
    print(f"Anda mendapatkan diskon sebesar 20% karena telah membeli tiket lebih dari 3 \nJadi total yang harus anda bayar sebesar: Rp {total_harga:,}")

# Struk Pemesanan
print("==========STRUK PEMESANAN==========")
print(f"Nama          : {nama}")
print(f"Umur          : {umur}")
print(f"Jenis kelamin : {jenis_kelamin}")
print("***********************************")
print(f"Kode maskapai : {kode}")
print(f"Tujuan        : {tujuan}")
print(f"Jenis kelas   : {kelas}")
print(f"Jumlah tiket  : {jumlah_tiket}")
print(f"Total harga   : {total_harga:,}")
print("...................................")
print("Terimakasih telah memilih maskapai kami \nSemoga perjalanan anda menyenangkan \nJangan lupa baca Bismillah sebelum lepas landas \nSelamat sampai tujuan")