import unittest
from reservation import Reservation

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.reservation = Reservation()

    def test_book_table(self):
        result = self.reservation.book_table("Alice", "T1", "19:00")
        self.assertEqual(result, "Reservasi berhasil")

    def test_confirm_reservation(self):
        self.reservation.book_table("Alice", "T1", "19:00")
        result = self.reservation.confirm_reservation("T1")
        self.assertEqual(result, "Reservasi dikonfirmasi")
