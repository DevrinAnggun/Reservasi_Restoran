from menu import Menu
from reservation import Reservation
from order import Order

menu = Menu()
reservation_system = Reservation()
order_system = Order()

# Menambahkan menu makanan
menu.add_item("M001", "Nasi Goreng", 25000)
menu.add_item("M002", "Ayam Bakar", 30000)
menu.add_item("M003", "Es Teh Manis", 5000)

# Simulasi reservasi
print(reservation_system.book_table("Alice", "T1", "19:00"))
print(reservation_system.confirm_reservation("T1"))

# Simulasi pemesanan
print(order_system.place_order("O001", "Alice", ["M001", "M002"]))
print(order_system.update_order_status("O001", "Diproses"))
