# This is what I've been ussing to test quickly the creation of offers with diferents values, manual and autobid.

import requests
import datetime as dt
import uuid

result = requests.post('http://127.0.0.1:5000/offer', json={
    "project_id": "b481b8c6-4be0-480b-a5a0-6721452b3d3a", "price": 0, "seller": "best_seller"})
result = requests.post('http://127.0.0.1:5000/offer', json={
    "project_id": "b481b8c6-4be0-480b-a5a0-6721452b3d3a", "price": 8, "seller": "best_seller", "min_price": 1})
print(result.text)
