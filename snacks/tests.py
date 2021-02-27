from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTest(SimpleTestCase):
    
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
