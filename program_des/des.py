import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

# Fungsi padding
def pad(teks):
    while len(teks) % 8 != 0:
        teks += ' '
    return teks

# Fungsi enkripsi
def encrypt(teks_plain, key):
    des = DES.new(key, DES.MODE_ECB)
    teks_terpad = pad(teks_plain)
    teks_enkripsi = des.encrypt(teks_terpad.encode('utf-8'))
    return base64.b64encode(teks_enkripsi).decode('utf-8')

# Fungsi dekripsi
def decrypt(teks_enkripsi, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(teks_enkripsi)
    teks_dekripsi = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return teks_dekripsi.rstrip()

# Fungsi untuk enkripsi dan dekripsi pada GUI
def enkripsi():
    teks_plain = entry_teks_plain.get()
    key_input = entry_kunci.get()
    
    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return

    if not teks_plain.strip():
        messagebox.showerror("Error", "Teks plain tidak boleh kosong.")
        return

    key = key_input.encode('utf-8')
    try:
        teks_enkripsi = encrypt(teks_plain, key)
        entry_teks_enkripsi.delete(0, tk.END)
        entry_teks_enkripsi.insert(tk.END, teks_enkripsi)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def dekripsi():
    teks_enkripsi = entry_teks_enkripsi.get()
    key_input = entry_kunci.get()
    
    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return

    if not teks_enkripsi.strip():
        messagebox.showerror("Error", "Teks enkripsi tidak boleh kosong.")
        return

    key = key_input.encode('utf-8')
    try:
        teks_dekripsi = decrypt(teks_enkripsi, key)
        entry_teks_dekripsi.delete(0, tk.END)
        entry_teks_dekripsi.insert(tk.END, teks_dekripsi)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk menutup aplikasi
def close_app():
    root.quit()

# Membuat jendela GUI
root = tk.Tk()
root.title("Enkripsi dan Dekripsi DES")

# Atur ukuran jendela
root.geometry("800x500")
root.configure(bg="#f0f0f0")

# Judul Aplikasi
tk.Label(root, text="Enkripsi dan Dekripsi dengan DES", font=('Helvetica', 16, 'bold'), bg="#f0f0f0").pack(pady=10)

# Frame utama
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True)

# Input teks plain
tk.Label(frame, text="Masukkan Teks Plain:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=0, column=0, pady=5, sticky="w")
entry_teks_plain = tk.Entry(frame, font=('Helvetica', 12), width=50)
entry_teks_plain.grid(row=0, column=1, pady=5)

# Input kunci
tk.Label(frame, text="Masukkan Kunci (8 karakter):", font=('Helvetica', 12), bg="#f0f0f0").grid(row=1, column=0, pady=5, sticky="w")
entry_kunci = tk.Entry(frame, font=('Helvetica', 12), width=50)
entry_kunci.grid(row=1, column=1, pady=5)

# Tombol Enkripsi
tk.Button(frame, text="Enkripsi", command=enkripsi, font=('Helvetica', 12), bg="#4CAF50", fg="#ffffff").grid(row=2, column=0, columnspan=2, pady=10)

# Output teks enkripsi
tk.Label(frame, text="Hasil Enkripsi:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=3, column=0, pady=5, sticky="w")
entry_teks_enkripsi = tk.Entry(frame, font=('Helvetica', 12), width=50)
entry_teks_enkripsi.grid(row=3, column=1, pady=5)

# Tombol Dekripsi
tk.Button(frame, text="Dekripsi", command=dekripsi, font=('Helvetica', 12), bg="#4CAF50", fg="#ffffff").grid(row=4, column=0, columnspan=2, pady=10)

# Output teks dekripsi
tk.Label(frame, text="Hasil Dekripsi:", font=('Helvetica', 12), bg="#f0f0f0").grid(row=5, column=0, pady=5, sticky="w")
entry_teks_dekripsi = tk.Entry(frame, font=('Helvetica', 12), width=50)
entry_teks_dekripsi.grid(row=5, column=1, pady=5)

# Tombol keluar
tk.Button(root, text="Keluar", command=close_app, font=('Helvetica', 12), bg="#f44336", fg="#ffffff").pack(pady=20)

# Menjalankan aplikasi
root.mainloop()