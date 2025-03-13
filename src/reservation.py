from config import Config

class Reservation:
    def __init__(self):
        self.reservations = {}

    def book_table(self, customer, table_id, time):
        if len(self.reservations) >= Config.MAX_TABLES:
            return "Tidak ada meja tersedia"
        if table_id in self.reservations:
            return "Meja sudah dipesan"
        
        self.reservations[table_id] = {"customer": customer, "time": time, "status": "Pending"}
        return "Reservasi berhasil"

    def confirm_reservation(self, table_id):
        if table_id in self.reservations and self.reservations[table_id]["status"] == "Pending":
            self.reservations[table_id]["status"] = "Dikonfirmasi"
            return "Reservasi dikonfirmasi"
        return "Reservasi tidak ditemukan"