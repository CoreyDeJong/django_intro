from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class SnickersTests(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'about.html')