from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import product_all


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django portfolio', created_by_id=1,
                               slug='django-portfolio', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test items response status
        """
        response = self.c.get(
            reverse('store:product_detail', args=['django-portfolio']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """
        Example: Using request factory
        """
        request = self.factory.get('/django-portfolio')
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
