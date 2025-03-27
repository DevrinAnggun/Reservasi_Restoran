import json
import os

RESERVATION_FILE = "data/reservations.json"

class ReservationManager:
    def __init__(self):
        self.reservations = self.load_reservations()

    def load_reservations(self):
        if os.path.exists(RESERVATION_FILE):
            with open(RESERVATION_FILE, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_reservations(self):
        with open(RESERVATION_FILE, "w") as file:
            json.dump(self.reservations, file, indent=4)

    def tambah_reservasi(self, nama, meja):
        self.reservations.append({"nama": nama, "meja": meja})
        self.save_reservations()
        print(f"Reservasi untuk {nama} di meja {meja} telah ditambahkan.")

    def lihat_reservasi(self):
        if not self.reservations:
            print("Tidak ada reservasi saat ini.")
        else:
            print("\n=== DAFTAR RESERVASI ===")
            for idx, res in enumerate(self.reservations, start=1):
                print(f"{idx}. {res['nama']} - Meja {res['meja']}")

    def hapus_reservasi(self):
        self.lihat_reservasi()
        try:
            index = int(input("Masukkan nomor reservasi yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.reservations):
                deleted_res = self.reservations.pop(index)
                self.save_reservations()
                print(f"Reservasi {deleted_res['nama']} di meja {deleted_res['meja']} telah dihapus.")
            else:
                print("Nomor reservasi tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")

reservation_manager = ReservationManager()
