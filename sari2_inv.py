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

@sari_inv.route("/items", methods=["GET"])
def get_items():
   category = request.args.get("category")
   result = [
      item for item in items
      if not category or item["category"].lower() == category.lower()
   ]
   if not result:
      return jsonify({"error": "No items found"}), 404
   return jsonify({"items": result}), 200

@sari_inv.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# ============================================================
# ENDPOINT 3 - POST /items  (Member B)
# ============================================================
# TODO: Member B
@sari_inv.route("/items", methods=["POST"])
def add_item():
  global next_id
  data = request.get_json(silent=True) or {}

  name = data.get("name")
  price = data.get("price")
  stock = data.get("stock")

  if not isinstance(name, str) or not name.strip():
    return jsonify({"error": "name is required and must be a non-empty string"}), 400
  if not is_number(price) or price < 0:
    return jsonify({"error": "price is required and must be a non-negative number"}), 400
  if not is_integer(stock) or stock < 0:
    return jsonify({"error": "stock is required and must be a non-negative integer"}), 400

  item = {
    "id" : next_id,
    "name" : name.strip(),
    "category" : data.get("category", "General"),
    "price" : price,
    "stock" : stock,
  }

  items.append(item)
  next_id += 1
  return jsonify(item), 201  


# ============================================================
# ENDPOINT 4 - PUT /items/<id>  (Member C)
# ============================================================
# TODO: Member C

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
#TODO: Member D
@sari_inv.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return jsonify({"message": f"Item {item_id} deleted"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    sari_inv.run(debug=True, port=5000)
