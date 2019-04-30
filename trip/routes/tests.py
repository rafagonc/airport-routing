import pytest
import random
import string
import os
from unittest import mock
from rest_framework import status


def id_generator(size=3, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

TEST_CSV_FILENAME = "test-input-file.csv"


@pytest.mark.urls("trip.urls")
class TestRoutesView():

    def create_dummy_csv_file(self, filename):
        with open(filename, "w+") as f:
            return f

    def remove_dummy_file(self, filename):
        os.remove(filename)

    def test_register_new_route(self, client):
        random_airport = id_generator(size=3)
        self.create_dummy_csv_file(TEST_CSV_FILENAME)
        with mock.patch('trip.routes.tasks.CSV_FILENAME') as test_filename:
            test_filename.return_value = TEST_CSV_FILENAME
            response = client.post("/routes/", {
                "source": "GRU",
                "destination": random_airport,
                "cost": 3
            })           
            assert response.status_code == status.HTTP_200_OK
            with open(TEST_CSV_FILENAME, "r+") as csv_file:
                assert ("GRU,%s,3" % random_airport) in csv_file.read()
            self.remove_dummy_file(TEST_CSV_FILENAME)

    def test_register_new_route_error(self, client):
        response = client.post("/routes/", {
            "source": "GRU",
            "destination": "MIM",
            "cost": 3
        })
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error"] == "There is already a cost for this route"

    def test_best_route_error(self, client):
        response = client.get("/routes/?source=ABC&destination=DEF")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error"] == "There is no possible route between these airports"

    def test_best_route_GRU_CDG(self, client):
        response = client.get("/routes/?source=GRU&destination=CDG")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["route"] == ["GRU", "BRC", "SCL", "ORL", "CDG"]
        assert response.json()["cost"] == 40

    def test_best_route_BRC_ORL(self, client):
        response = client.get("/routes/?source=BRC&destination=ORL")
        assert response.status_code == status.HTTP_200_OK
        
        assert response.json()["route"] == ["BRC", "SCL", "ORL"]
        assert response.json()["cost"] == 25
