from django.test import TestCase
from django.urls import reverse

from .models import Product

class ProductListTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Product1', price=10, store='Store1', store_link='https://example.com/product1')
        Product.objects.create(name='Product2', price=20, store='Store2', store_link='https://example.com/product2')
        Product.objects.create(name='Product3', price=30, store='Store3', store_link='https://example.com/product3')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/product_list/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('product_list'))
        self.assertTemplateUsed(response, 'viewlist/product_list.html')

    def test_view_returns_correct_products(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(len(response.context['object_list']), 3)

    def test_view_orders_products_correctly(self):
        response = self.client.get(reverse('product_list'))
        products = response.context['object_list']
        self.assertEqual(products[0].name, 'Product3')
        self.assertEqual(products[1].name, 'Product2')
        self.assertEqual(products[2].name, 'Product1')
