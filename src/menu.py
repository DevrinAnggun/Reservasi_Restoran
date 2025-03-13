class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, price):
        self.items[item_id] = {"name": name, "price": price}

    def get_menu(self):
        return self.items