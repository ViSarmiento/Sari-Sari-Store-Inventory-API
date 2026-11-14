### Sari-Sari Store Inventory API

from flask import Flask, jsonify, request

sari_inv = Flask(__name__)

items = [
  {"id": 1, "name": "Pancit Canton", "category": "Noodles", "price": 25, "stock": 40},
  {"id": 2, "name": "Safeguard", "category": "Toiletries", "price": 30, "stock": 31},
  {"id": 3, "name": "Skyflakes", "category": "Crackers", "price": 8, "stock": 28},
  {"id": 4, "name": "Milo", "category": "Powdered Drink", "price": 15, "stock": 14},
]
next_id = 5


def find_item(item_id):
  return next((item for item in items if item["id"] == item_id), None)

def is_number(value):
  return isinstance(value, (int, float)) and not isinstance(value, bool)

def is_integer(value):
  return isinstance(value, int) and not isinstance(value, bool)

# ============================================================
# ENDPOINTS 1 & 2 - GET /items and GET /items/<id>  (Member A)
# ============================================================
# TODO: Member A


# ============================================================
# ENDPOINT 3 - POST /items  (Member B)
# ============================================================
# TODO: Member B


# ============================================================
# ENDPOINT 4 - PUT /items/<id>  (Member C)
# ============================================================
#andrei CCCCCCC

@sari_inv.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
  """Update the price and/or stock of one item."""
  item = find_item(item_id)
  if item is None:                          # 404: item doesn't exist
    return jsonify({"error": "Item not found"}), 404

  data = request.get_json(silent=True)      # read the JSON body
  if not isinstance(data, dict) or ("price" not in data and "stock" not in data):
    return jsonify({"error": "Send price and/or stock"}), 400
  

  # Use the new value if sent, otherwise keep the old one
  price = data.get("price", item["price"])
  stock = data.get("stock", item["stock"])

  if not is_number(price) or price < 0:     # 400: bad price
    return jsonify({"error": "price must be a non-negative number"}), 400
  if not is_integer(stock) or stock < 0:    # 400: bad stock
    return jsonify({"error": "stock must be a non-negative integer"}), 400

  item["price"] = price                     # all good, save the changes
  item["stock"] = stock
  return jsonify(item), 200                 # 200: return the updated item

# ============================================================
# ENDPOINT 5 - DELETE /items/<id>  (Member D)
# ============================================================
# TODO: Member D


if __name__ == "__main__":
    sari_inv.run(debug=True, port=5000)