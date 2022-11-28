from fastapi.testclient import TestClient
import unittest
from main import app

# Routing de l'API
client = TestClient(app)


class TestFastApi(unittest.TestCase):

    def test_read_main(self):
        """
        Test le client fastapi pour vérifier la connexion au serveur
        """
        response = client.get("/")
        assert response.status_code == 200
