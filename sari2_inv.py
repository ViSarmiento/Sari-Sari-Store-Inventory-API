### Sari-Sari Store Inventory API

From flask import Flask, jsonify, request

sari_inv = Flask(__name__)

items = [
  {"id": 1, "name": "Pancit Canton", "category": "Noodles", "price": 25, "stock": 40},
  {"id": 2, "name": "Safeguard", "category": "Toiletries", "price": 30, "stock": 31},
  {"id": 3, "name": "Skyflakes", "category": "Crackers", "price": 8, "stock": 28},
  {"id": 4, "name": "Milo", "category": "Powdered Drink", "price": 15, "stock": 14},
]
next_id = 4


def find_item(item_id):
  return next((item for item in items if item["id"] == item_id), None)

def is_number(value):
  return isinstance(value, (int, float)) and not isinstance(value, bool)

def is_integer(value):
  return isinstance(value, int) and not isinstance(value, bool)
