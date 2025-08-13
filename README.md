# Aplikasi management pasien rumah sakit

Aplikasi rumah sakit ini digunakan untuk menambahkan data pasien untuk rumah sakit

Aplikasi ini dibuat untuk tugas capstone project kelas purwadhika modul 1

Aplikasi ini ditujukan untuk user seperti:
1. Administrasi
2. Perawat 
3. Hospitality

### Terdiri dari 4 Fungsi (Create, Read, Update, Delete)

### Create (Menambahkan data baru)
Dalam menu create dapat menambahkan data pasien baru
Data pasien tersebut berupa:

[ID pasien, Nama, Umur, Jenis_Kelamin, alamat, no_hp, diagnosa, tanggal_masuk, Kelas/Ruangan, Dokter, dan status)

1. Menampilkan daftar ID**:Nama** yang sudah ada sebagai referensi (Agar user experience nya bagus)
2. Input ID pasien (integer) dengan cek duplikat (tidak boleh sama)
3. Validasi Umur agar pasti integer
4. Validasi Jenis Kelamin hanya L/P
5. Pilih Kelas/Ruangan via nomor dari data_kelas_ranap
6. Pilih Status via nomor dari STATUS_OPTIONS
7. Pilih Dokter via nomor dari data_dokter

### Read (Melihat data)
Dalam menu Read terdapat beberapa fungsi seperti:
1. Lihat semua pasien
2. Lihat berdasarkan ID pasien
3. Lihat berdasarkan nama pasien
4. Lihat berdasarkan Ruangan/kelas
5. Lihat berdasarkan Dokter yang menangani

### Update
dalam menu update ini di kategorikan menjadi 2 update agar lebih berpusat:
1. Update untuk informasi pasien (Nama umur hingga nomor hp)
2. Update untuk perawatan pasien (Diagnosa hingga status pasien)
3. Submenu Biodata: Nama, Umur (Enter = tidak diubah; angka = int), Jenis Kelamin (L/P), Alamat, No HP
4. Submenu Perawatan: Diagnosa, Tanggal Masuk, Kelas (pilih nomor), Dokter (pilih nomor), Status (pilih nomor)
5. Header submenu menampilkan Nama + ID pasien yang sedang diedit

### Delete
1. Delete feature disini dapat menghapus by ID pasien dengan konfirmasi sebelum benar-benar menghapus data pasien
2. Menampilkan semua data untuk memastikan ID
3. Input ID (validasi angka) → tampilkan konfirmasi (y/n) dengan Nama + ID
4. Submenu Hapus Data Pasien / Kembali ke Main Menu

## Flow Alur Aplikasi

```text
Main Menu
├── 1) Lihat Data Pasien
│   ├── Lihat semua
│   ├── Lihat berdasarkan ID
│   ├── Lihat berdasarkan Nama
│   ├── Lihat berdasarkan Kelas/Ruangan (nomor dari data_kelas_ranap)
│   └── Lihat berdasarkan Dokter (nomor dari data_dokter)
│
├── 2) Tambah Data Pasien
│   ├── 1) Tambah Pasien → form input + validasi + pilih via nomor
│   └── 2) Kembali ke Main Menu
│
├── 3) Ubah Data Pasien
│   ├── 1) Ubah Data → pilih ID → submenu Biodata/Perawatan
│   └── 2) Kembali ke Main Menu
│
├── 4) Hapus Data Pasien
│   ├── 1) Hapus Data Pasien → pilih ID → konfirmasi (y/n)
│   └── 2) Kembali ke Main Menu
│
└── 5) Keluar
