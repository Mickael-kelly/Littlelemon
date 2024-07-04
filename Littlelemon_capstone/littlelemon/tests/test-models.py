# tests.py
from django.test import TestCase
from ..restaurant.models import Menu

class MenuTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        item = self.item
        self.assertEqual(str(item), "IceCream : 80")
