import json
import os

ORDER_FILE = "data/orders.json"

class OrderManager:
    def __init__(self):
        self.orders = self.load_orders()

    def load_orders(self):
        if os.path.exists(ORDER_FILE):
            with open(ORDER_FILE, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_orders(self):
        with open(ORDER_FILE, "w") as file:
            json.dump(self.orders, file, indent=4)

    def tambah_order(self):
        meja = input("Nomor Meja: ")
        menu = input("Nama Menu: ")
        jumlah = input("Jumlah: ")

        self.orders.append({"meja": meja, "menu": menu, "jumlah": jumlah})
        self.save_orders()
        print(f"Order {menu} untuk meja {meja} sebanyak {jumlah} telah ditambahkan.")

    def lihat_order(self):
        if not self.orders:
            print("Tidak ada order saat ini.")
        else:
            print("\n=== DAFTAR ORDER ===")
            for idx, order in enumerate(self.orders, start=1):
                print(f"{idx}. Meja {order['meja']} - {order['menu']} x {order['jumlah']}")

    def hapus_order(self):
        self.lihat_order()
        try:
            index = int(input("Masukkan nomor order yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.orders):
                deleted_order = self.orders.pop(index)
                self.save_orders()
                print(f"Order {deleted_order['menu']} di meja {deleted_order['meja']} telah dihapus.")
            else:
                print("Nomor order tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")

order_manager = OrderManager()
