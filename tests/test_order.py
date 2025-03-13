import unittest
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()

    def test_place_order(self):
        result = self.order.place_order("O001", "Alice", ["M001", "M002"])
        self.assertEqual(result, "Pemesanan berhasil")

    def test_update_order_status(self):
        self.order.place_order("O001", "Alice", ["M001", "M002"])
        result = self.order.update_order_status("O001", "Diproses")
        self.assertEqual(result, "Status pemesanan diperbarui")
