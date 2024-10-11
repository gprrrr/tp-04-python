import unittest
from unittest.mock import patch
from main import get_bike_data


class TestFlaskApp(unittest.TestCase):
    def test_get_bike_data(self):
        mock_data = {
            "total_count": 2,
            "features": [
                {
                    "properties": {
                        "libelle": 136,
                        "etat_connexion": "CONNECTÉ",
                        "nom": "RUE CHAMBORD",
                        "y": 3.133873,
                        "x": 50.62972,
                        "nb_places_dispo": 0,
                        "nb_velos_dispo": 0,
                    },
                },
                {
                    "properties": {
                        "libelle": 136,
                        "etat_connexion": "CONNECTÉ",
                        "nom": "PAVÉ DE LILLE",
                        "y": 3.133873,
                        "x": 50.62972,
                        "nb_places_dispo": 10,
                        "nb_velos_dispo": 10,
                    },
                },
                {
                    "properties": {
                        "libelle": 136,
                        "etat_connexion": "DECONNECTÉ",
                        "nom": "RUE TOTO",
                        "y": 3.456783,
                        "x": 50.66782,
                        "nb_places_dispo": 0,
                        "nb_velos_dispo": 0,
                    }
                }
            ],
        }

        with unittest.mock.patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = mock_data
            result = get_bike_data()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["properties"]["nom"], "RUE CHAMBORD")
        self.assertEqual(result[1]["properties"]["nom"], "PAVÉ DE LILLE")


if __name__ == "__main__":
    unittest.main()
