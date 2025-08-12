# Aplikasi management pasien rumah sakit

## Terdiri dari 4 Fungsi (Create, Read, Update, Delete)

### Create (Menambahkan data baru)
Dalam menu create dapat menambahkan data pasien baru
Data pasien tersebut berupa:

[ID pasien, Nama, Umur, Jenis_Kelamin, alamat, no_hp, diagnosa, tanggal_masuk, Kelas/Ruangan, Dokter, dan status)

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

### Delete
Delete feature disini dapat menghapus by ID pasien dengan konfirmasi sebelum benar-benar menghapus


Alur Menu Aplikasi 
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
