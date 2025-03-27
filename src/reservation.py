from src.storage import load_data, save_data

def tambah_reservasi():
    reservations = load_data("reservations.json")

    print("\n=== Tambah Reservasi ===")
    nama = input("Masukkan nama pelanggan: ")
    meja = input("Pilih nomor meja: ")
    nomor_hp = input("Masukkan nomor HP: ")

    while True:
        dp = input("Masukkan jumlah DP (Minimal Rp50.000): ")
        try:
            dp = int(dp)
            if dp >= 50000:
                break
            else:
                print("❌ DP minimal Rp50.000. Silakan coba lagi.")
        except ValueError:
            print("❌ Masukkan angka yang valid.")

    reservations.append({
        "nama": nama,
        "meja": meja,
        "nomor_hp": nomor_hp,
        "dp": dp
    })

    save_data("reservations.json", reservations)
    print("\n✅ Reservasi berhasil ditambahkan!")

def lihat_reservasi():
    reservations = load_data("reservations.json")

    print("\n=== Daftar Reservasi ===")
    if not reservations:
        print("Tidak ada reservasi.")
        return

    for res in reservations:
        print(f"Nama: {res['nama']}, Meja: {res['meja']}, No HP: {res['nomor_hp']}, DP: Rp{res['dp']}")

def hapus_reservasi():
    reservations = load_data("reservations.json")

    print("\n=== Hapus Reservasi ===")
    lihat_reservasi()
    nama = input("Masukkan nama pelanggan yang ingin dihapus: ")

    new_reservations = [r for r in reservations if r["nama"] != nama]

    if len(new_reservations) < len(reservations):
        save_data("reservations.json", new_reservations)
        print("✅ Reservasi berhasil dihapus!")
    else:
        print("❌ Reservasi tidak ditemukan.")
