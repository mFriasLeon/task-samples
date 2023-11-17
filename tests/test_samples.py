"""Naralabs task: Managing samples.

Tests to check APIs to introduce and get samples.
Using Pytest
"""

from pip import main
from fastapi.testclient import TestClient
from main import app
from fastapi import status
import json
from datetime import datetime
from dateutil import parser
import numpy as np
from database.connection import  naralabs_db

client = TestClient(app)

# Mocks to introduce samples
sample_mock = {
  "monitored_id": 1,
  "sample_name": "Breast Biopsy",
  "diagnosis": "Ductal carcinoma in situ",
  "date": "2022-02-21T08:20:01.52+01:00",
  "tissue_size": 3
}


# Test functions

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_insert_sample():
    """checking response status and json of sample insert function
    """
    response = client.post("/samples/insert",json=sample_mock)
    assert response.status_code == 201
    assert response.json() == { "message": "Sample  created successfully"}


def test_get_samples():
    """checking response status by monitored_id and sample_name.
    """
    monitored_id = "1"
    name = "Breast Biopsy"

    response = (client.get("/samples/get/"+monitored_id+"/"+name))
    assert response.status_code == 200
    samples = json.loads(response.content)


            
def test_get_sample_error():
    """checking if a put a sample_name which is not in the database
    """
    monitored_id = "1"
    name = "colon"
    response = (client.get("/samples/get/"+monitored_id+"/"+name))

    assert response.status_code == 404
    assert response.json() == {'detail': 'Sample not found'}


