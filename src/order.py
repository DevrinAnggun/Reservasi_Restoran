class Order:
    order_rules = {
        "max_items_per_order": 5,
        "order_time_limit": "30 minutes"
    }
    
    def __init__(self):
        self.orders = {}

    def place_order(self, order_id, customer, items):
        if len(items) > self.order_rules["max_items_per_order"]:
            return "Melebihi batas pemesanan"
        
        self.orders[order_id] = {"customer": customer, "items": items, "status": "Dipesan"}
        return "Pemesanan berhasil"

    def update_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]["status"] = status
            return "Status pemesanan diperbarui"
        return "Pemesanan tidak ditemukan"