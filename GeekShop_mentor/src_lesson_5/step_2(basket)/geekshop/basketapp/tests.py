from django.test import TestCase
from .models import Basket
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


class TestBasket(TestCase):

    def setUp(self):
        for_test_user = ShopUser(username='Test', email='test@test.com')
        category = ProductCategory(name='Test')
        product = Product(name='TestProduct', category=category, price=10, quantity=10)
        self.b = Basket(user=for_test_user, product=product)

    def test_str(self):
        # создадим пользователя
        self.assertEqual(str(self.b), 'Test: TestProduct')

    def test_other(self):
        # создадим пользователя
        self.assertEqual(self.b.other(), 'Other')
