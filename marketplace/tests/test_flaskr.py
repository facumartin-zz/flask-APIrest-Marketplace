# These are the tests I've created, the first is to test the endpoint and test that the in memory starts empty.
# The second one is to test the create new project functionality. I consider at least two more to be done.
# Test creating offers in a project by id, and another one to test the definition of the winning offer and auto-bid functionality.

import requests
import json
import os
import sys


def test_empty_db():
    """Start with a blank database."""
    response = requests.get('http://127.0.0.1:5000/projects')
    assert "[]" in response.text
    assert 200 == response.status_code


def test_post_project():
    """Test that creating a new project work."""
    requests.post('http://127.0.0.1:5000/projects', json={"description": "description",
                                                          "requirements": "requirements", "max_budget": 10, "bids_deadline": '2021-05-17'})
    response = requests.get('http://127.0.0.1:5000/projects')
    assert 200 == response.status_code
    assert response.text != "[]"


# another tests to be done are:
"""
def test_post_offer():
    requests.get('http://127.0.0.1:5000/projects')
    firstprojectID = deserialize object and get a project ID, just to post an offer 
    request.post('http://127.0.0.1:5000/projects', json={
     "project_id": "first_project_ID", "price": 79}}))
    request.get('http://127.0.0.1:5000/projects/first_project_ID)
    assert that offer was created

"""

"""
def test_winning_offer():
    requests.get('http://127.0.0.1:5000/projects')
    firstprojectID = deserialize object and get a project ID, just to post an offer 
    request.post('http://127.0.0.1:5000/projects', json={
    "project_id": "first_project_ID", "price": 79}}))
    request.get('http://127.0.0.1:5000/projects/first_project_ID)
    post here another offer and assert that the winner is the correct option, there are many cases to test here about the auto-bid functionality.
"""
