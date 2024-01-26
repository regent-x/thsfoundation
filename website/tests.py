from django.test import SimpleTestCase



# Create your tests here.

class TestWelcomePage(SimpleTestCase):

    def test_url_path(self):
        response = self.client.get('/welcome')
        self.assertEqual(response.status_code, 200)
