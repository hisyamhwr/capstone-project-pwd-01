### DATA RUMAH SAKIT DR. HISYAM HAWARI ###

data_pasien = [
    {
        "ID_Pasien" : 1001,
        "nama": "Budiono Siregar",
        "umur": 22,
        "jenis_kelamin": "L",
        "alamat": "Jakarta",
        "no_hp": "081234567890",
        "diagnosa": "Tipes",
        "tanggal_masuk": "2025-08-05",
        "kelas": "Kelas II",
        "dokter": "Dr. Rini Yulianti",
        "status": "Rawat Inap"
    },
    {
        "ID_Pasien" : 1002,
        "nama": "Mimi Peri",
        "umur": 45,
        "jenis_kelamin": "P",
        "alamat": "Bogor",
        "no_hp": "081234567890",
        "diagnosa": "Usus Buntu",
        "tanggal_masuk": "2025-08-05",
        "kelas": "Kelas 1",
        "dokter": "Dr. Anton Al Huda",
        "status": "Rawat Inap"
    },
    {
        "ID_Pasien" : 1003,
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
    "Dr. Mursyid Feriawan",
    "Dr. Febri Istiqamah"
]

data_kelas_ranap = [
    "VVIP",
    "VIP",
    "Kelas I",
    "Kelas II",
    "Kelas III"
]

data_status = [
    "Rawat Inap",
    "Rawat Jalan",
    "Pulang"
]

# ---------------------------------------------------------- #
### Function 1 : READ

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
    print("-----------------------------")

# Lihat Semua Pasien
def lihat_semua():
    if not data_pasien:
        print('Data tidak ditemukan')
    else:
        print('Berikut data pasien di RS dr HISYAM HAWARI:')
        for pasien in data_pasien:
            tampilkan_data(pasien)

# Lihat dari ID pasien
def lihat_dari_id():
    id_input = input('Masukkan ID pasien: ').strip()
    if not id_input.isdigit():
        print('ID harus berupa angka.')
        return

    cari_id = int(id_input)
    for pasien in data_pasien:
        if pasien['ID_Pasien'] == cari_id:
            tampilkan_data(pasien)
            return
    print('Data yang anda cari tidak ditemukan.')

# Lihat dari nama pasien
def lihat_dari_nama():
    cari_nama = input('Masukkan nama pasien: ').lower()
    pasienData = False
    for pasien in data_pasien:
        if cari_nama in pasien['nama'].lower():
            tampilkan_data(pasien)
            pasienData = True
    if not pasienData:
        print('Data yang anda cari tidak ditemukan.')

# Lihat dari kelas / ruangan
def lihat_dari_kelas():
    if not data_kelas_ranap:
        print("Daftar kelas/ruangan belum didefinisikan.")
        return

    print("\nDaftar Kelas/Ruangan yang tersedia:")
    for i, k in enumerate(data_kelas_ranap, 1):
        print(f"{i}. {k}")

    while True:
        pilihan = input(f"Pilih nomor kelas/ruangan (1-{len(data_kelas_ranap)}): ").strip()
        if pilihan.isdigit():
            indexRuangan = int(pilihan) - 1
            if 0 <= indexRuangan < len(data_kelas_ranap):
                kelas_dicari = data_kelas_ranap[indexRuangan]
                break
        print("Pilihan tidak valid. Silakan pilih nomor kelas/ruangan yang tersedia.")

    ketemu = False
    for pasien in data_pasien:
        if pasien.get('kelas') == kelas_dicari:
            tampilkan_data(pasien)
            ketemu = True

    if not ketemu:
        print(f"Tidak ada pasien untuk kelas/ruangan {kelas_dicari}.")

# Lihat dari dokter yang menangani
def lihat_dari_dokter():
    print("\nDaftar dokter RS dr. HISYAM HAWARI:")
    for i, dokter in enumerate(data_dokter, 1):
        print(f"{i}. {dokter}")

    while True:
        pilihan = input("Pilih nomor dokter yang ingin ditampilkan datanya: ").strip()
        if pilihan.isdigit():
            indexDokter = int(pilihan) - 1
            if 0 <= indexDokter < len(data_dokter):
                dokter_dicari = data_dokter[indexDokter]
                break
        print("Pilihan tidak valid. Silakan pilih nomor dokter yang tersedia.")

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
        print("2. Melihat Data Pasien Berdasarkan ID")
        print("3. Melihat Data Pasien Dengan Nama Pasien")
        print("4. Menampilkan Data Pasien Berdasarkan Kelas/Ruangan")
        print("5. Menampilkan Data Pasien Berdasarkan Dokter")
        print("6. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == "1":
            lihat_semua()
        elif pilihan == "2":
            lihat_dari_id()
        elif pilihan == "3":
            lihat_dari_nama()
        elif pilihan == "4":
            lihat_dari_kelas()
        elif pilihan == "5":
            lihat_dari_dokter()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# ---------------------------------------------------------- #
### Function 2 : CREATE

def tambah_pasien():
    print("\n===== Tambah Data Pasien Baru =====")

    # 1) Daftar ID yang sudah ada
    print("\nDaftar ID Pasien RS DR. HISYAM HAWARI:")
    if data_pasien:
        for dp in data_pasien:
            print(f"- {dp['ID_Pasien']}: {dp['nama']}")
    else:
        print("(Belum ada data pasien)")

    # 2) Input ID sesuai dengan angka terakhir (x) biar gampang menambahkan
    while True:
        id_input = input("Masukkan ID Pasien (100X): ").strip()
        if not id_input.isdigit():
            print("ID harus berupa angka. Coba lagi.")
            continue

        id_pasien = int(id_input)

        id_duplicate = next((p for p in data_pasien if p["ID_Pasien"] == id_pasien), None)
        if id_duplicate is not None:
            print(f"ID {id_pasien} sudah digunakan oleh '{id_duplicate['nama']}'. Masukkan ID lain.")
            continue
        break

    print(f"ID {id_pasien} bisa digunakan, Silahkan isi data pasien berikut:")

    # 3) Input informasi pasien
    nama = input("Masukkan nama pasien: ").strip()

    while True:
        umur_input = input("Masukkan umur pasien: ").strip()
        if umur_input.isdigit():
            umur = int(umur_input)
            break
        print("Umur harus angka. Coba lagi.")

    while True:
        jenis_kelamin = input("Masukkan jenis kelamin pasien (L/P): ").strip().upper()
        if jenis_kelamin in ("L", "P"):
            break
        print("Input tidak valid. Gunakan L atau P.")

    alamat = input("Masukkan alamat pasien: ").strip()
    no_hp = input("Masukkan no HP pasien: ").strip()

    # 4) Input Keterangan Kesehatan
    diagnosa = input("Masukkan diagnosa pasien: ").strip()
    tanggal_masuk = input("Masukkan tanggal masuk (YYYY-MM-DD): ").strip()

    # 5) Input ruangan dan status
    print("\nPilih Kelas/Ruangan:")
    for i, k in enumerate(data_kelas_ranap, 1):
        print(f"{i}. {k}")
    while True:
        k_in = input(f"Pilih nomor (1-{len(data_kelas_ranap)}): ").strip()
        if k_in.isdigit() and 1 <= int(k_in) <= len(data_kelas_ranap):
            kelas = data_kelas_ranap[int(k_in) - 1]
            break
        print("Pilihan tidak valid. Coba lagi.")


    print("\nPilih Status:")
    for i, s in enumerate(data_status, 1):
        print(f"{i}. {s}")
    while True:
        s_in = input(f"Pilih nomor (1-{len(data_status)}): ").strip()
        if s_in.isdigit() and 1 <= int(s_in) <= len(data_status):
            status = data_status[int(s_in) - 1]
            break
        print("Pilihan tidak valid. Coba lagi.")


    print("\nDaftar dokter yang tersedia:")
    for i, dokter in enumerate(data_dokter, 1):
        print(f"{i}. {dokter}")
    while True:
        pilihan_dokter = input(f"Pilih nomor dokter penanggung jawab (1-{len(data_dokter)}): ").strip()
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

def menu_tambah_pasien():
    while True:
        print("\nMenu Tambah Data Pasien:")
        print("1. Tambah Pasien")
        print("2. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# --------------------------------------------------- #
# --- FUNCTION 3 : UPDATE

def ubah_data_pasien():

    def lihat_seluruh_data():
        if not data_pasien:
            print("Belum ada data pasien.")
        else:
            for pasien in data_pasien:
                tampilkan_data(pasien)

    lihat_seluruh_data()
    try:
        id_target = int(input("Masukkan ID Pasien yang ingin diubah: ").strip())
    except ValueError:
        print("Input tidak valid.")
        return

    index = None
    for i, p in enumerate(data_pasien):
        if p["ID_Pasien"] == id_target:
            index = i
            break

    if index is None:
        print("ID Pasien tidak ditemukan.")
        return

    pasien = data_pasien[index]

    # ubah biodata
    def submenu_biodata():
        while True:
            print("\n")
            print("##### UBAH BIODATA PASIEN #####")
            print(f"1. Nama               [{pasien['nama']}]")
            print(f"2. Umur               [{pasien['umur']}]")
            print(f"3. Jenis Kelamin (L/P)[{pasien['jenis_kelamin']}]")
            print(f"4. Alamat             [{pasien['alamat']}]")
            print(f"5. No HP              [{pasien['no_hp']}]")
            print("6. Batal/Kembali")
            print("\n")
            pilih = input("Pilih data biodata yang ingin diubah (1-6): ").strip()

            if pilih == "1":
                pasien['nama'] = input(f"Nama baru [{pasien['nama']}]: ").strip() or pasien['nama']
                print("Nama pasien telah diperbarui.")
            elif pilih == "2":
                baru = input(f"Umur baru [{pasien['umur']}]: ").strip()
                if baru == "":
                    print("Umur tidak diubah.")
                elif baru.isdigit():
                    pasien['umur'] = int(baru)
                    print("Umur telah diperbarui.")
                else:
                    print("Umur harus menggunakan angka. Perubahan dibatalkan.")
            elif pilih == "3":
                baru = input(f"Jenis Kelamin baru (L/P) [{pasien['jenis_kelamin']}]: ").strip().upper()
                if baru in ("L", "P", ""):
                    pasien['jenis_kelamin'] = baru if baru != "" else pasien['jenis_kelamin']
                    print("Jenis kelamin pasien telah diperbarui.")
                else:
                    print("Input tidak valid (gunakan L atau P).")
            elif pilih == "4":
                pasien['alamat'] = input(f"Alamat baru [{pasien['alamat']}]: ").strip() or pasien['alamat']
                print("Alamat pasien telah diperbarui.")
            elif pilih == "5":
                pasien['no_hp'] = input(f"No HP baru [{pasien['no_hp']}]: ").strip() or pasien['no_hp']
                print("No HP pasien telah diperbarui.")
            elif pilih == "6":
                print("Kembali ke menu utama UPDATE.")
                break
            else:
                print("Pilihan tidak valid.")

    # ubah keterangan perawatan
    def submenu_perawatan():
        while True:
            print('-----------------------------')
            print(f"Pilih data yang ingin diubah dari pasien {pasien['nama']} (ID: {pasien['ID_Pasien']})")
            print("##### UBAH KETERANGAN PERAWATAN #####")
            print(f"1. Diagnosa           [{pasien['diagnosa']}]")
            print(f"2. Tanggal Masuk      [{pasien['tanggal_masuk']}]")
            print(f"3. Kelas/Ruangan      [{pasien['kelas']}]")
            print(f"4. Dokter             [{pasien['dokter']}]")
            print(f"5. Status             [{pasien['status']}]")
            print("6. Batal/Kembali")
            pilih = input("Pilih data perawatan yang ingin diubah (1-6): ").strip()

            if pilih == "1":
                pasien['diagnosa'] = input(f"Diagnosa baru [{pasien['diagnosa']}]: ").strip() or pasien['diagnosa']
                print("Diagnosa pasien telah diperbarui.")
            elif pilih == "2":
                pasien['tanggal_masuk'] = input(f"Tanggal Masuk baru (YYYY-MM-DD) [{pasien['tanggal_masuk']}]: ").strip() or pasien['tanggal_masuk']
                print("Tanggal masuk pasien telah diperbarui.")
            elif pilih == "3":
                print("\nPilih Kelas/Ruangan:")
                for i, k in enumerate(data_kelas_ranap, 1):
                    print(f"{i}. {k}")
                inp = input(f"Pilih nomor kelas (1-{len(data_kelas_ranap)}) atau isikan kosong untuk batal: ").strip()
                if inp == "":
                    pass
                elif inp.isdigit() and 1 <= int(inp) <= len(data_kelas_ranap):
                    pasien['kelas'] = data_kelas_ranap[int(inp) - 1]
                    print("Kelas/Ruangan pasien telah diperbarui.")
                else:
                    print("Pilihan tidak valid.")
            elif pilih == "4":
                print("Daftar dokter yang tersedia:")
                for i, d in enumerate(data_dokter, 1):
                    print(f"{i}. {d}")
                pilihan_dokter = input(f"Pilih nomor dokter (1-{len(data_dokter)}) atau isikan kosong untuk batal: ").strip()
                if pilihan_dokter.isdigit():
                    indexDokter = int(pilihan_dokter) - 1
                    if 0 <= indexDokter < len(data_dokter):
                        pasien['dokter'] = data_dokter[indexDokter]
                        print("Dokter yang di assign telah diperbarui.")
                    else:
                        print("Nomor dokter tidak valid.")
                elif pilihan_dokter == "":
                    pass
                else:
                    print("Input tidak valid.")
            elif pilih == "5":
                print("\nPilih Status:")
                for i, s in enumerate(data_status, 1):
                    print(f"{i}. {s}")
                inp = input(f"Pilih nomor status (1-{len(data_status)}) atau isikan kosong untuk batal: ").strip()
                if inp == "":
                    pass
                elif inp.isdigit() and 1 <= int(inp) <= len(data_status):
                    pasien['status'] = data_status[int(inp) - 1]
                    print("Status pasien telah diperbarui.")
                else:
                    print("Pilihan tidak valid.")
            elif pilih == "6":
                print("Kembali ke menu utama UPDATE.")
                break
            else:
                print("Pilihan tidak valid.")

    while True:
        print('-----------------------------')
        print("Pilih data yang ingin diubah dari pasien {nama} (ID: {id})".format(nama=pasien['nama'], id=pasien['ID_Pasien']))
        print("1. Ubah Biodata Pasien   (Nama, Umur, JK, Alamat, No HP)")
        print("2. Ubah Keterangan Perawatan (Diagnosa, Tanggal Masuk, Kelas, Dokter dan Status)")
        print("3. Batal/Kembali")
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

def menu_ubah_data_pasien():
    while True:
        print("\nMenu Ubah Data Pasien:")
        print("1. Ubah Data")
        print("2. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            ubah_data_pasien()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# --------------------------------------------------- #
# --- FUNCTION : DELETE

def hapus_data_pasien():
    if not data_pasien:
        print("Belum ada data pasien untuk dihapus.")
        return

    lihat_semua()

    id_input = input("Masukkan ID Pasien yang ingin dihapus: ").strip()
    if not id_input.isdigit():
        print("Input tidak valid.")
        return
    nomor = int(id_input)

    target = next((p for p in data_pasien if p["ID_Pasien"] == nomor), None)
    if target is None:
        print("ID Pasien tidak ditemukan.")
        return

    while True:
        konfirmasi = input(
            f"Yakin ingin menghapus pasien {target['nama']} (ID: {target['ID_Pasien']})? (y/n): "
        ).strip().lower()
        if konfirmasi in ("y", "n"):
            break
        print("Input tidak valid. Ketik 'y' untuk ya atau 'n' untuk tidak.")

    if konfirmasi == "n":
        print("Dibatalkan. Data tidak dihapus.")
        return

    data_pasien.remove(target)
    print("Data pasien berhasil dihapus!")

def menu_hapus_data_pasien():
    while True:
        print("\nMenu Hapus Data Pasien:")
        print("1. Hapus Data Pasien")
        print("2. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            hapus_data_pasien() 
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# --------------------------------------------------- #
## Function : MENU

def main_menu():
    while True: 
        print("\n============= SELAMAT DATANG ==============")
        print("\n### SISTEM CRUD DATA PASIEN RUMAH SAKIT ###")
        print("\n====== RUMAH SAKIT DR. HISYAM HAWARI ======")
        print("\n")
        print("1. Lihat Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Ubah Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        pilihan = input("Silahkan pilih menu (1-5) sesuai kebutuhan: ").strip()

        if pilihan == "1":
            menu_lihat_data_pasien()
        elif pilihan == "2":
            menu_tambah_pasien()
        elif pilihan == "3":
            menu_ubah_data_pasien()
        elif pilihan == "4":
            menu_hapus_data_pasien()
        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan ulangi.")

# Main Menu
if __name__ == "__main__":
    main_menu()
# ------------------------------------------------------ #