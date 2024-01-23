from django.test import SimpleTestCase



# Create your tests here.
class TestHomePage(SimpleTestCase):

    def test_url_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestSignupPage(SimpleTestCase):

    def test_url_path(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)


class TestWelcomePage(SimpleTestCase):

    def test_url_path(self):
        response = self.client.get('/welcome')
        self.assertEqual(response.status_code, 200)
