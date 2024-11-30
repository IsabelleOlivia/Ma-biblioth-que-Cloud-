import unittest
from app import app


class TestLibraryApp(unittest.TestCase):

    def setUp(self):
        """Configuration avant les tests"""
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        """Test de la route index"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_emprunter_livre(self):
        """Test de l'emprunt d'un livre"""
        response = self.app.post('/emprunter', json={
            'id_livre': 1,
            'id_lecteur': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Livre emprunté avec succès',
                      response.get_json()['message'])


if __name__ == '__main__':
    unittest.main()
