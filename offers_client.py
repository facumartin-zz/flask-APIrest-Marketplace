# This is what I've been ussing to test quickly the creation of offers with diferents values, manual and autobid.

import requests
import datetime as dt
import uuid

result = requests.post('http://127.0.0.1:5000/offer', json={
    "project_id": "98edba5a-d482-423d-8d1a-33cf8bd3cf8a", "price": 300, "seller": "best_seller"})
result = requests.post('http://127.0.0.1:5000/offer', json={
    "project_id": "98edba5a-d482-423d-8d1a-33cf8bd3cf8a", "price": 100, "seller": "best_seller", "min_price": 50})
print(result.text)
