from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class TestHomePage(SimpleTestCase):

    def test_url_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestSignupPage(SimpleTestCase):

    def test_url_path(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)




