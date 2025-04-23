import json
import os
from datetime import datetime

DATA_DIR = "data"
RESERVATION_FILE = os.path.join(DATA_DIR, "reservations.json")
ORDER_FILE = os.path.join(DATA_DIR, "orders.json")

MENU_MAKANAN = {
    1: ("Paket Ayam Goreng", 20000),
    2: ("Paket Ayam Geprek", 22000),
    3: ("Pecel Lele", 18000),
    4: ("Nasi Padang", 25000),
    5: ("Es Teller", 10000),
    6: ("Es Teh", 5000),
    7: ("Air Putih", 3000),
    8: ("Es Jeruk", 7000),
}

# Buat folder data kalau belum ada
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def tambah_reservasi():
    nama = input("Nama Pelanggan: ")
    meja = input("Nomor Meja: ")

    # Ambil tanggal hari ini
    tanggal_reservasi = datetime.now().strftime("%d-%m-%Y")
    
    data = load_data(RESERVATION_FILE)
    data.append({
        "nama": nama, 
        "meja": meja, 
        "tanggal": tanggal_reservasi, 
        "status_pembayaran": "belum"  # Pastikan status pembayaran terisi
    })
    save_data(RESERVATION_FILE, data)
    
    print(f"Reservasi untuk {nama} di meja {meja} pada tanggal {tanggal_reservasi} telah ditambahkan.")

def lihat_reservasi():
    data = load_data(RESERVATION_FILE)
    if not data:
        print("Tidak ada reservasi saat ini.")
    else:
        print("\n=== DAFTAR RESERVASI ===")
        for idx, res in enumerate(data, start=1):
            # Pastikan status_pembayaran ada
            status = res.get('status_pembayaran', 'belum')
            print(f"{idx}. {res['nama']} - Meja {res['meja']} - Tanggal {res['tanggal']} - Status: {status}")

def order_menu():
    orders = load_data(ORDER_FILE)
    meja = input("Nomor Meja: ")

    while True:
        print("\n=== MENU MAKANAN & MINUMAN ===")
        for no, (nama, harga) in MENU_MAKANAN.items():
            print(f"{no}. {nama} - Rp {harga:,}")

        try:
            pilihan = int(input("Pilih nomor menu (0 untuk selesai): "))
            if pilihan == 0:
                break
            if pilihan not in MENU_MAKANAN:
                print("Menu tidak valid.")
                continue
            jumlah = int(input("Jumlah: "))
            nama_menu, harga = MENU_MAKANAN[pilihan]
            orders.append({
                "meja": meja,
                "menu": nama_menu,
                "jumlah": jumlah,
                "total": jumlah * harga
            })
            print(f"{jumlah} x {nama_menu} ditambahkan untuk meja {meja}.")
        except ValueError:
            print("Input tidak valid.")

    save_data(ORDER_FILE, orders)
    print("Order telah disimpan.")

def lihat_order():
    orders = load_data(ORDER_FILE)
    if not orders:
        print("Belum ada order.")
        return
    print("\n=== SEMUA ORDER ===")
    for idx, order in enumerate(orders, start=1):
        print(f"{idx}. Meja {order['meja']} - {order['menu']} x {order['jumlah']} | Total: Rp {order['total']:,}")

def cetak_struk_total():
    orders = load_data(ORDER_FILE)
    if not orders:
        print("Tidak ada order untuk dicetak.")
        return

    total_semua = sum(order["total"] for order in orders)

    print("\n" + "=" * 35)
    print("         STRUK TOTAL ORDER         ")
    print("=" * 35)
    print(f"{'No':<4}{'Meja':<6}{'Menu':<18}{'Qty':<5}{'Subtotal':>8}")
    print("-" * 35)

    for idx, order in enumerate(orders, start=1):
        print(f"{idx:<4}{order['meja']:<6}{order['menu']:<18}{order['jumlah']:<5}Rp {order['total']:>7,}")

    print("-" * 35)
    print(f"{'TOTAL SEMUA:':<28}Rp {total_semua:,.2f}")
    print("=" * 35)
    print("   Terima kasih telah memesan!   ")
    print("=" * 35 + "\n")

    # Menghapus reservasi yang sudah dibayar
    data_reservasi = load_data(RESERVATION_FILE)
    data_reservasi_baru = [res for res in data_reservasi if res.get("status_pembayaran", "belum") != "sudah"]
    save_data(RESERVATION_FILE, data_reservasi_baru)

    print("Semua reservasi yang sudah dibayar telah dihapus.")

def hapus_reservasi():
    data_reservasi = load_data(RESERVATION_FILE)
    data_order = load_data(ORDER_FILE)

    lihat_reservasi()
    try:
        index = int(input("Masukkan nomor reservasi yang ingin dihapus: ")) - 1
        if 0 <= index < len(data_reservasi):
            deleted = data_reservasi.pop(index)
            save_data(RESERVATION_FILE, data_reservasi)

            # Hapus semua order terkait dengan meja yang dihapus
            nomor_meja = deleted['meja']
            data_order_baru = [order for order in data_order if order['meja'] != nomor_meja]
            save_data(ORDER_FILE, data_order_baru)

            print(f"Reservasi {deleted['nama']} di meja {nomor_meja} telah dihapus.")
            print(f"Semua order untuk meja {nomor_meja} juga telah dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")

def main():
    while True:
        print("\n=== SISTEM RESERVASI RESTORAN ===")
        print("1. Tambah Reservasi")
        print("2. Lihat Reservasi")
        print("3. Order Menu")
        print("4. Lihat Semua Order")
        print("5. Cetak Struk Total Order")

        # Hanya tampilkan menu "Hapus Reservasi" jika ada reservasi yang status pembayarannya "belum bayar"
        if any(res.get("status_pembayaran", "belum bayar") == "belum bayar" for res in load_data(RESERVATION_FILE)):
            print("6. Hapus Reservasi")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_reservasi()
        elif pilihan == "2":
            lihat_reservasi()
        elif pilihan == "3":
            order_menu()
        elif pilihan == "4":
            lihat_order()
        elif pilihan == "5":
            cetak_struk_total()
        elif pilihan == "6":
            hapus_reservasi()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
