import os
import json

# Folder tempat menyimpan data
DATA_DIR = "data"

# Pastikan folder "data" ada
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Fungsi untuk membuat file jika belum ada
def cek_dan_buat_file(filename):
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)  # File dibuat kosong dengan array JSON

# Fungsi untuk membaca data dari file JSON
def load_data(filename):
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        return []  # Jika file tidak ada, kembalikan list kosong

    with open(file_path, "r") as file:
        try:
            return json.load(file)  # Baca data dari file
        except json.JSONDecodeError:
            return []  # Jika file rusak, kembalikan list kosong

# Fungsi untuk menyimpan data ke file JSON
def save_data(filename, data):
    file_path = os.path.join(DATA_DIR, filename)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Pastikan semua file penting dibuat
cek_dan_buat_file("reservations.json")
cek_dan_buat_file("orders.json")
cek_dan_buat_file("history.json")
