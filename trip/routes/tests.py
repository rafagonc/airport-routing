import pytest
import random
import string
from rest_framework import status


def id_generator(size=3, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


@pytest.mark.urls("trip.urls")
class TestRoutesView():
    def test_register_new_route(self, client):
        response = client.post("/routes/", {
            "source": "GRU",
            "destination": id_generator(size=3),
            "cost": 3
        })
        assert response.status_code == status.HTTP_200_OK

    def test_register_new_route_error(self, client):
        response = client.post("/routes/", {
            "source": "GRU",
            "destination": "MIM",
            "cost": 3
        })
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error"] == "Ja existe um custo para esta rota"

    def test_best_route_GRU_CDG(self, client):
        response = client.get("/routes/?source=GRU&destination=CDG")
        import pdb
        pdb.set_trace()
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["route"] == ["GRU", "BRC", "SCL", "ORL", "CDG"]
        assert response.json()["cost"] == 40

    def test_best_route_BRC_ORL(self, client):
        response = client.get("/routes/?source=BRC&destination=ORL")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["route"] == ["BRC", "SCL", "ORL"]
        assert response.json()["cost"] == 25
