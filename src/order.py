from src.reservation import lihat_reservasi
from src.storage import load_data, save_data

def tambah_order():
    orders = load_data("orders.json")
    print("\n=== Tambah Order ===")

    lihat_reservasi()  # Memastikan user melihat daftar reservasi sebelum order

    nama = input("Masukkan nama pelanggan: ")
    makanan = input("Masukkan makanan yang dipesan: ")
    minuman = input("Masukkan minuman yang dipesan: ")

    orders.append({
        "nama": nama,
        "makanan": makanan,
        "minuman": minuman
    })

    save_data("orders.json", orders)

    print("\n✅ Order berhasil ditambahkan!")
    print(f"Nama: {nama}, Makanan: {makanan}, Minuman: {minuman}")

def lihat_order():
    orders = load_data("orders.json")

    print("\n=== Daftar Order ===")
    if not orders:
        print("Tidak ada order.")
        return

    for order in orders:
        print(f"Nama: {order['nama']}, Makanan: {order['makanan']}, Minuman: {order['minuman']}")

def hapus_order():
    orders = load_data("orders.json")

    print("\n=== Hapus Order ===")
    lihat_order()
    nama = input("Masukkan nama pelanggan yang ordernya ingin dihapus: ")

    new_orders = [o for o in orders if o["nama"] != nama]

    if len(new_orders) < len(orders):
        save_data("orders.json", new_orders)
        print("✅ Order berhasil dihapus!")
    else:
        print("❌ Order tidak ditemukan.")
