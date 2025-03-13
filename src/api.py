from flask import Flask, jsonify # type: ignore
from menu import Menu
from reservation import Reservation
from order import Order

app = Flask(__name__)
menu = Menu()
reservation_system = Reservation()
order_system = Order()

@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify(menu.get_menu())

@app.route("/reservations", methods=["GET"])
def get_reservations():
    return jsonify(reservation_system.reservations)

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(order_system.orders)

if __name__ == "__main__":
    app.run(debug=True)
