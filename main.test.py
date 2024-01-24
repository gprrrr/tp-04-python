import unittest
from unittest.mock import patch
from main import get_bike_data

class TestFlaskApp(unittest.TestCase):
    def test_get_bike_data(self):
        mock_data = {
            "total_count": 2,
            "results": [
                {
                    "libelle": 136,
                    "etatconnexion": "CONNECTÉ",
                    "nom": "RUE CHAMBORD",
                    "geo": {"lon": 3.133873, "lat": 50.62972},
                    "nbplacesdispo": 0,
                    "nbvelosdispo": 0,
                },
                {
                    "libelle": 270,
                    "etatconnexion": "CONNECTÉ",
                    "nom": "PAVÉ DE LILLE",
                    "geo": {"lon": 3.130098, "lat": 50.664211},
                    "nbplacesdispo": 18,
                    "nbvelosdispo": 2,
                },
                {
                   "libelle": 275,
                   "etatconnexion": "DÉCONNECTÉ",
                   "nom": "Rue VOLTAIRE",
                   "geo": {"lon": 3.130098, "lat": 50.664211},
                   "nbplacesdispo": 0,
                   "nbvelosdispo": 0,
                },
            ],
        }

        with unittest.mock.patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = mock_data
            result = get_bike_data()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["nom"], "RUE CHAMBORD")
        self.assertEqual(result[1]["nom"], "PAVÉ DE LILLE")

if __name__ == "__main__":
    unittest.main()
