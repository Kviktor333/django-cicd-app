from django.test import TestCase

class SimpleTest(TestCase):
    def test_homepage_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)