import unittest

from app.api.main import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        response = self.app.post('/predict', json={"feature1": 5.0, "feature2": 2.3, "feature3": 3.3, "feature4": 1.0})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))
        self.assertTrue("class" in data[0])
        self.assertTrue("confidence" in data[0])


if __name__ == '__main__':
    unittest.main()
