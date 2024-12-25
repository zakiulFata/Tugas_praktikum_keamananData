CAESAR CIPHER
# Program Enkripsi dan Deskripsi Text

## Deskripsi
Aplikasi GUI untuk enkripsi dan dekripsi teks menggunakan metode Caesar Cipher. Program ini dibuat dengan Python dan Tkinter.

## Cara Menjalankan
1. Pastikan Python 3 terinstal.
2. Simpan kode program di file, misalnya `program_enkripsi.py`.
3. Jalankan dengan perintah:
   ```bash
   python program_enkripsi.py
Cara Penggunaan di GUI :
Masukkan teks di kolom Plaintext.
Masukkan nilai pergeseran (1-25).
Klik Enkripsi untuk menghasilkan ciphertext atau Deskripsi untuk teks asli.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ALGORITMA DES
# Program Enkripsi dan Dekripsi dengan DES

## Deskripsi
Aplikasi GUI ini menggunakan algoritma **DES (Data Encryption Standard)** untuk melakukan enkripsi dan dekripsi teks. Program ini dibuat dengan Python menggunakan pustaka Tkinter untuk antarmuka grafis.

## Fitur
1. Enkripsi teks menggunakan algoritma DES.
2. Dekripsi teks terenkripsi kembali ke teks asli.
3. Validasi input kunci (harus terdiri dari 8 karakter).

## Cara Menjalankan
1. Pastikan Python 3 dan pustaka `pycryptodome` sudah terinstal.
   - Instal pustaka `pycryptodome` dengan perintah:
     ```bash
     pip install pycryptodome
     ```
2. Simpan kode di file bernama `des_gui.py` (atau nama lain yang Anda pilih).
3. Jalankan program dengan perintah:
   ```bash
   python des_gui.py
   
Berikut adalah isi README singkat untuk program DES yang Anda buat:

markdown
Salin kode
# Program Enkripsi dan Dekripsi dengan DES

## Deskripsi
Aplikasi GUI ini menggunakan algoritma **DES (Data Encryption Standard)** untuk melakukan enkripsi dan dekripsi teks. Program ini dibuat dengan Python menggunakan pustaka Tkinter untuk antarmuka grafis.

## Fitur
1. Enkripsi teks menggunakan algoritma DES.
2. Dekripsi teks terenkripsi kembali ke teks asli.
3. Validasi input kunci (harus terdiri dari 8 karakter).

## Cara Menjalankan
1. Pastikan Python 3 dan pustaka `pycryptodome` sudah terinstal.
   - Instal pustaka `pycryptodome` dengan perintah:
     ```bash
     pip install pycryptodome
     ```
2. Simpan kode di file bernama `des_gui.py` (atau nama lain yang Anda pilih).
3. Jalankan program dengan perintah:
   ```bash
   python des_gui.py
Cara Penggunaan :
Masukkan teks yang ingin dienkripsi pada kolom Masukkan Teks Plain.
Masukkan kunci (8 karakter) pada kolom Masukkan Kunci.
Klik tombol Enkripsi untuk mendapatkan hasil teks terenkripsi.
Untuk dekripsi, masukkan teks terenkripsi dan kunci yang sama, lalu klik tombol Dekripsi.
Klik tombol Keluar untuk menutup aplikasi.
Catatan
Kunci harus terdiri dari 8 karakter.
Pastikan teks dan kunci tidak kosong untuk menghindari kesalahan.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
STEGANOGRAFI
# Steganografi Tool

## Deskripsi
Aplikasi **Steganografi Tool** adalah program GUI berbasis Python untuk menyembunyikan dan menampilkan pesan rahasia di dalam gambar menggunakan teknik steganografi. Program ini memanfaatkan pustaka `stegano` untuk menyisipkan dan mengungkap pesan dari gambar.

## Fitur
1. **Sembunyikan Pesan**: Menyisipkan pesan rahasia ke dalam gambar.
2. **Tampilkan Pesan**: Mengungkap pesan tersembunyi dari gambar.

## Persyaratan
- Python 3.x
- Pustaka `stegano`
- Pustaka `tkinter` (sudah termasuk dalam instalasi Python)

## Cara Instalasi
1. Pastikan Python 3 sudah terinstal di komputer Anda.
2. Instal pustaka `stegano` menggunakan pip:
   ```bash
   pip install stegano
Cara Menjalankan
Simpan kode di file bernama steganografi_tool.py.
Jalankan program dengan perintah:
bash
Salin kode
python steganografi_tool.py

Cara Penggunaan :
1. Menyembunyikan Pesan
  Klik tombol Sembunyikan Pesan.
  Pilih gambar sumber (format .png atau .jpg).
  Masukkan pesan rahasia yang ingin disisipkan.
  Pilih lokasi dan nama file untuk menyimpan gambar hasil.
  Klik tombol Sembunyikan untuk menyimpan gambar dengan pesan rahasia.
2. Menampilkan Pesan
  Klik tombol Tampilkan Pesan.
  Pilih gambar yang mengandung pesan tersembunyi.
  Klik tombol Tampilkan Pesan untuk melihat pesan yang tersembunyi.
  Catatan
  Hanya format gambar .png yang didukung untuk menyimpan gambar dengan pesan tersembunyi.
  Pastikan pesan tidak terlalu panjang agar kompatibel dengan gambar yang dipilih.
