import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.order import order_manager
from src.reservation import reservation_manager
from src.receipt import cetak_struk_dp
from src.history import lihat_riwayat
from src.edit_reservation import edit_reservasi

def main():
    while True:
        print("\n=== SISTEM RESERVASI RESTORAN ===")
        print("1. Tambah Reservasi")
        print("2. Lihat Reservasi")
        print("3. Hapus Reservasi")
        print("4. Tambah Order")
        print("5. Lihat Order")  # Dipindahkan
        print("6. Hapus Order")  # Dipindahkan
        print("7. Edit Reservasi")
        print("8. Riwayat Reservasi & Order Selesai")
        print("9. Cetak Struk DP")
        print("10. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama Pelanggan: ")
            meja = input("Nomor Meja: ")
            reservation_manager.tambah_reservasi(nama, meja)
        elif pilihan == "2":
            reservation_manager.lihat_reservasi()
        elif pilihan == "3":
            reservation_manager.hapus_reservasi()
        elif pilihan == "4":
            order_manager.tambah_order()
        elif pilihan == "5":
            order_manager.lihat_order()
        elif pilihan == "6":
            order_manager.hapus_order()
        elif pilihan == "7":
            edit_reservasi()
        elif pilihan == "8":
            lihat_riwayat()
        elif pilihan == "9":
            cetak_struk_dp()
        elif pilihan == "10":
            print("Terima kasih telah menggunakan sistem reservasi restoran!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
