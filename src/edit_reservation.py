from src.reservation import reservation_manager

def edit_reservasi():
    reservation_manager.lihat_reservasi()
    try:
        index = int(input("Masukkan nomor reservasi yang ingin diedit: ")) - 1
        if 0 <= index < len(reservation_manager.reservations):
            nama_baru = input("Nama baru: ")
            meja_baru = input("Nomor meja baru: ")
            reservation_manager.reservations[index] = {"nama": nama_baru, "meja": meja_baru}
            reservation_manager.save_reservations()
            print("Reservasi berhasil diperbarui!")
        else:
            print("Nomor reservasi tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid.")
