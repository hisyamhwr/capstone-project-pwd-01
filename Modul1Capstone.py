### DATA RUMAH SAKIT DR. HISYAM HAWARI ###

data_pasien = [
    {
        "ID_Pasien" : 1,
        "nama": "Budiono Siregar",
        "umur": 22,
        "jenis_kelamin": "L",
        "alamat": "Jakarta",
        "no_hp": "081234567890",
        "diagnosa": "Tipes",
        "tanggal_masuk": "2025-08-05",
        "kelas": "Kelas A",
        "dokter": "Dr. Rini Yulianti",
        "status": "Rawat Inap"
    },
        {
        "ID_Pasien" : 2,
        "nama": "Mimi Peri",
        "umur": 45,
        "jenis_kelamin": "P",
        "alamat": "Bogor",
        "no_hp": "081234567890",
        "diagnosa": "Usus Buntu",
        "tanggal_masuk": "2025-08-05",
        "kelas": "Kelas A",
        "dokter": "Dr. Anton Al Huda",
        "status": "Rawat Inap"
    },
        {
        "ID_Pasien" : 3,
        "nama": "Udin Sedunia",
        "umur": 11,
        "jenis_kelamin": "L",
        "alamat": "Depok",
        "no_hp": "081234567890",
        "diagnosa": "Demam Berdarah",
        "tanggal_masuk": "2025-08-05",
        "kelas": "VIP",
        "dokter": "Dr. Mursyid Feriawan",
        "status": "Rawat Inap"
    }
]

data_dokter = [
    "Dr. Rini Yulianti",
    "Dr. Anton Al Huda",
    "Dr. Siti Inshani",
    "Dr. Mursyid Feriawan"
    "Dr. Febri Istiqamah"
]

# data_pasien_update = data_pasien.copy()
# ID_Pasien = 0

# ---------------------------------------------------------- #
### Function 1 : READ
### Untuk membaca data pasien yang ada di dalam data_pasien[]

def tampilkan_data(pasien):
    print("\n----------------------------")
    print(f"ID Pasien     : {pasien['ID_Pasien']}")
    print(f"Nama          : {pasien['nama']}")
    print(f"Umur          : {pasien['umur']}")
    print(f"Jenis Kelamin : {pasien['jenis_kelamin']}")
    print(f"Alamat        : {pasien['alamat']}")
    print(f"No HP         : {pasien['no_hp']}")
    print(f"Diagnosa      : {pasien['diagnosa']}")
    print(f"Tanggal Masuk : {pasien['tanggal_masuk']}")
    print(f"Kelas         : {pasien['kelas']}")
    print(f"Dokter        : {pasien['dokter']}")
    print(f"Status        : {pasien['status']}")
    print("\n----------------------------")

# Lihat data semua pasien
def lihat_semua():
    if not data_pasien:
        print('Data tidak ditemukan')
    else:
        print('Berikut data pasien di RS dr HISYAM HAWARI:')
        for pasien in data_pasien:
            tampilkan_data(pasien)

# Lihat data pasien dengan nama
def lihat_dari_nama():
    cari_nama = input('Masukkan nama pasien: ').lower()
    pasienData = False
    for pasien in data_pasien:
            if cari_nama in pasien['nama'].lower():
                tampilkan_data(pasien)
                pasienData = True
    if not pasienData:
        print('Data yang anda cari tidak ditemukan.')

# Lihat data pasien menggunakan kelas 
def lihat_dari_kelas():
    cari_nama = input('Masukkan nama kelas(ruangan) pasien:').lower()
    pasienData = False
    for pasien in data_pasien:
        if cari_nama in pasien['kelas'].lower():
            tampilkan_data(pasien)
            pasienData = True
    if not pasienData:
        print('Data yang anda cari tidak ditemukan.')

# Lihat data pasien berdasarkan dokter
def lihat_dari_dokter():
    print("\nDaftar dokter RS dr. HISYAM HAWARI:")
    for i, dokter in enumerate(data_dokter, 1):
        print(f"{i}. {dokter}")

    # Validasi input dokter
    while True:
        pilihan = input("Pilih nomor dokter yang ingin ditampilkan datanya: ")
        if pilihan.isdigit():
            indexDokter = int(pilihan) - 1
            if 0 <= indexDokter < len(data_dokter):
                dokter_dicari = data_dokter[indexDokter]
                break
        print("Pilihan tidak valid. Silakan pilih nomor dokter yang tersedia.")

    # Tampilkan data pasien berdasarkan dokter yang dipilih
    ketemu = False
    for pasien in data_pasien:
        if pasien['dokter'] == dokter_dicari:
            tampilkan_data(pasien)
            ketemu = True
    if not ketemu:
        print(f"Tidak ada pasien untuk {dokter_dicari}.")


def menu_lihat_data_pasien():
    while True:
        print("\nMenu Lihat Data Pasien:")
        print("1. Melihat Seluruh Data Pasien")
        print("2. Melihat Data Pasien Dengan Nama Pasien")
        print("3. Menampilkan Data Pasien Berdasarkan Kelas/Ruangan")
        print("4. Menampilkan Data Pasien Berdasarkan Dokter")
        print("5. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            lihat_semua()
        elif pilihan == "2":
            lihat_dari_nama()
        elif pilihan == "3":
            lihat_dari_kelas()
        elif pilihan == "4":
            lihat_dari_dokter()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
    
# menu_lihat_data_pasien()
# ---------------------------------------------------------- #


# ---------------------------------------------------------- #
### Function 2 : CREATE
### Untuk membuat data pasien baru
def tambah_pasien():
    print("\n=== Tambah Data Pasien Baru ===")
    id_pasien = len(data_pasien) + 1

    nama = input("Masukkan nama pasien: ")
    
    # Casting umur untuk diubah ke int
    while True:
        umur = input("Masukkan umur pasien: ")
        if umur.isdigit():
            umur = int(umur)
            break
        else:
            print('Umur harus angka coba lagi.')
    # ---------------------------------

    jenis_kelamin = input("Masukkan jenis kelamin pasien (L/P): ")
    alamat = input("Masukkan alamat pasien: ")
    no_hp = input("Masukkan no HP pasien: ")
    diagnosa = input("Masukkan diagnosa pasien: ")
    tanggal_masuk = input("Masukkan tanggal masuk (YYYY-MM-DD): ")
    kelas = input("Masukkan ruangan/kelas pasien: ")
    status = input("Masukkan status pasien (Rawat Inap/Jalan/Pulang): ")
    
    # Pilih dokter dari daftar
    print("\nDaftar dokter yang tersedia:")
    for i, dokter in enumerate(data_dokter, 1):
        print(f"{i}. {dokter}")
    while True:
        pilihan_dokter = input(f"Pilih nomor dokter penanggung jawab (1-{len(data_dokter)}): ")
        if pilihan_dokter.isdigit():
            indexDokter = int(pilihan_dokter) - 1
            if 0 <= indexDokter < len(data_dokter):
                dokter = data_dokter[indexDokter]
                break
        print("Pilihan tidak valid. Silakan pilih nomor dokter yang tersedia.")

    pasien_baru = {
        "ID_Pasien": id_pasien,
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "alamat": alamat,
        "no_hp": no_hp,
        "diagnosa": diagnosa,
        "tanggal_masuk": tanggal_masuk,
        "kelas": kelas,
        "dokter": dokter,
        "status": status
    }
    data_pasien.append(pasien_baru)
    print("Data pasien berhasil ditambahkan!")
# --------------------------------------------------- #


# --------------------------------------------------- #
# --- FUNCTION 3 : UPDATE
# Function yang digunakan untuk mengubah data pasien ---
def ubah_data_pasien():
    if not data_pasien:
        print("Belum ada data pasien untuk diubah.")
        return

    def lihat_seluruh_data():
        if not data_pasien:
            print("Belum ada data pasien.")
        else:
            for pasien in data_pasien:
                tampilkan_data(pasien)

    lihat_seluruh_data()
    try:
        id_target = int(input("Masukkan ID Pasien yang ingin diubah: "))
    except ValueError:
        print("Input tidak valid.")
        return

    # Cari index pasien berdasarkan ID
    index = None
    for i, p in enumerate(data_pasien):
        if p["ID_Pasien"] == id_target:
            index = i
            break

    if index is None:
        print("ID Pasien tidak ditemukan.")
        return

    pasien = data_pasien[index]

    # --- Submenu: Ubah Biodata ---
    def submenu_biodata():
        while True:
            print("=== UBAH BIODATA PASIEN ===")
            print(f"1. Nama               [{pasien['nama']}]")
            print(f"2. Umur               [{pasien['umur']}]")
            print(f"3. Jenis Kelamin (L/P)[{pasien['jenis_kelamin']}]")
            print(f"4. Alamat             [{pasien['alamat']}]")
            print(f"5. No HP              [{pasien['no_hp']}]")
            print("6. Batal/Kembali")  # angka terakhir untuk batal
            pilih = input("Pilih data biodata yang ingin diubah (1-6): ").strip()

            if pilih == "1":
                pasien['nama'] = input(f"Nama baru [{pasien['nama']}]: ") or pasien['nama']
                print("✔ Nama diperbarui.")
            elif pilih == "2":
                baru = input(f"Umur baru [{pasien['umur']}]: ")
                pasien['umur'] = baru if baru != "" else pasien['umur']
                print("✔ Umur diperbarui.")
            elif pilih == "3":
                baru = input(f"Jenis Kelamin baru (L/P) [{pasien['jenis_kelamin']}]: ").upper()
                if baru in ("L", "P", ""):
                    pasien['jenis_kelamin'] = baru if baru != "" else pasien['jenis_kelamin']
                    print("✔ Jenis kelamin diperbarui.")
                else:
                    print("Input tidak valid (gunakan L atau P).")
            elif pilih == "4":
                pasien['alamat'] = input(f"Alamat baru [{pasien['alamat']}]: ") or pasien['alamat']
                print("✔ Alamat diperbarui.")
            elif pilih == "5":
                pasien['no_hp'] = input(f"No HP baru [{pasien['no_hp']}]: ") or pasien['no_hp']
                print("✔ No HP diperbarui.")
            elif pilih == "6":
                print("Kembali ke menu utama UPDATE.")
                break
            else:
                print("Pilihan tidak valid.")

    # --- Submenu: Ubah Keterangan Perawatan ---
    def submenu_perawatan():
        while True:
            print("=== UBAH KETERANGAN PERAWATAN ===")
            print(f"1. Diagnosa           [{pasien['diagnosa']}]")
            print(f"2. Tanggal Masuk      [{pasien['tanggal_masuk']}]")
            print(f"3. Kelas/Ruangan      [{pasien['kelas']}]")
            print(f"4. Dokter             [{pasien['dokter']}]")
            print(f"5. Status             [{pasien['status']}]")
            print("6. Batal/Kembali")  # angka terakhir untuk batal
            pilih = input("Pilih data perawatan yang ingin diubah (1-6): ").strip()

            if pilih == "1":
                pasien['diagnosa'] = input(f"Diagnosa baru [{pasien['diagnosa']}]: ") or pasien['diagnosa']
                print("✔ Diagnosa diperbarui.")
            elif pilih == "2":
                pasien['tanggal_masuk'] = input(f"Tanggal Masuk baru (YYYY-MM-DD) [{pasien['tanggal_masuk']}]: ") or pasien['tanggal_masuk']
                print("✔ Tanggal masuk diperbarui.")
            elif pilih == "3":
                pasien['kelas'] = input(f"Kelas/Ruangan baru [{pasien['kelas']}]: ") or pasien['kelas']
                print("✔ Kelas/Ruangan diperbarui.")
            elif pilih == "4":
                print("Daftar dokter yang tersedia:")
                for i, d in enumerate(data_dokter, 1):
                    print(f"{i}. {d}")
                pilihan_dokter = input(f"Pilih nomor dokter (1-{len(data_dokter)}) atau enter untuk batal: ").strip()
                if pilihan_dokter.isdigit():
                    idx = int(pilihan_dokter) - 1
                    if 0 <= idx < len(data_dokter):
                        pasien['dokter'] = data_dokter[idx]
                        print("✔ Dokter diperbarui.")
                    else:
                        print("Nomor dokter tidak valid.")
                elif pilihan_dokter == "":
                    pass  # batal
                else:
                    print("Input tidak valid.")
            elif pilih == "5":
                baru = input(f"Status baru (Rawat Inap/Jalan/Pulang) [{pasien['status']}]: ")
                pasien['status'] = baru if baru != "" else pasien['status']
                print("✔ Status diperbarui.")
            elif pilih == "6":
                print("Kembali ke menu utama UPDATE.")
                break
            else:
                print("Pilihan tidak valid.")

    # --- Menu Utama UPDATE: klasifikasi biodata vs perawatan ---
    while True:
        print("=== MENU UPDATE PASIEN (ID: {}) ===".format(pasien['ID_Pasien']))
        print("1. Ubah Biodata Pasien   (Nama, Umur, JK, Alamat, No HP)")
        print("2. Ubah Keterangan Perawatan (Diagnosa, Tanggal Masuk, Kelas, Dokter dan Status)")
        print("3. Batal/Kembali")  # angka terakhir untuk batal
        pm = input("Pilih menu (1-3): ").strip()
        if pm == "1":
            submenu_biodata()
        elif pm == "2":
            submenu_perawatan()
        elif pm == "3":
            print("Selesai update. Kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid.")
# --------------------------------------------------- #


# --------------------------------------------------- #
# --- FUNCTION : DELETE
# Function yang digunakan untuk hapus Data Pasien ---
def hapus_data_pasien():
    if not data_pasien:
        print("Belum ada data pasien untuk dihapus.")
        return
    lihat_semua()
    try:
        nomor = int(input("Masukkan ID Pasien yang ingin dihapus: "))
        index = None
        for i, pasien in enumerate(data_pasien):
            if pasien["ID_Pasien"] == nomor:
                index = i
                break
        if index is None:
            print("ID Pasien tidak ditemukan.")
            return
        del data_pasien[index]
        print("Data pasien berhasil dihapus!")
    except ValueError:
        print("Input tidak valid.")
# --------------------------------------------------- #


# --------------------------------------------------- #
## Function : MENU
def main_menu():
    while True: 
        print("\n============= SELAMAT DATANG ==============")
        print("\n=== SISTEM CRUD DATA PASIEN RUMAH SAKIT ===")
        print("\n======= RUMAH SAKIT DR HISYAM HAWARI =======")
        print("1. Lihat Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Ubah Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            menu_lihat_data_pasien()
        elif pilihan == "2":
            tambah_pasien()
        elif pilihan == "3":
            ubah_data_pasien()
        elif pilihan == "4":
            hapus_data_pasien()
        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan ulangi.")

# --- Jalankan Program ---
if __name__ == "__main__":
    main_menu()
# ------------------------------------------------------ # 