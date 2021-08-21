from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class First_App_Tests(SimpleTestCase):

    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_status_not_404(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 404)
    
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_if_file_not_found(self):
        url = "http://127.0.0.1:8000/aboutme"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_about_page_template_not_used(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateNotUsed(response, 'home.html')
