from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
