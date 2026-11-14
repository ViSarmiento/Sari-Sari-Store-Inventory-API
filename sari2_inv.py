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
# TODO: Member C


# ============================================================
# ENDPOINT 5 - DELETE /items/<id>  (Member D)
# ============================================================
# TODO: Member D


if __name__ == "__main__":
    sari_inv.run(debug=True, port=5000)