# This is a cliente I've been ussing to test quickly the creation of projects with diferents values.
import requests
import datetime as dt
import uuid


result = requests.post('http://127.0.0.1:5000/projects', json={"description": "description",
                                                               "requirements": "requirements", "max_budget": 10, "bids_deadline": '2021-05-17', "owner": "project owner"})
print(result.text)
