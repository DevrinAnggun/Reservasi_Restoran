from src.reservation import tambah_reservasi, lihat_reservasi, hapus_reservasi
from src.order import tambah_order, lihat_order, hapus_order

def main():
    while True:
        print("\n=== SISTEM RESERVASI RESTORAN ===")
        print("1. Tambah Reservasi")
        print("2. Lihat Reservasi")
        print("3. Hapus Reservasi")
        print("4. Tambah Order")
        print("5. Lihat Order")
        print("6. Hapus Order")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_reservasi()
        elif pilihan == "2":
            lihat_reservasi()
        elif pilihan == "3":
            hapus_reservasi()
        elif pilihan == "4":
            lihat_reservasi()  # Memastikan user melihat reservasi sebelum order
            tambah_order()
        elif pilihan == "5":
            lihat_order()
        elif pilihan == "6":
            hapus_order()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan sistem reservasi restoran!")
            break
        else:
            print("❌ Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
