import unittest
import random
from factures import Product, InvoiceLine, Invoice
import itertools
import factory
from faker.providers import BaseProvider

list_of_products_names = ['Horse', 'Dog', 'Chicken', 'Octopus', 'Whale']


class ProductProvider(BaseProvider):
    """
    This custom povider returns product names
    """
    def product_name(self):
        return random.choice(list_of_products_names)


# We add the Product provider to factory
factory.Faker.add_provider(ProductProvider)


# We create our product factory
class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    name = factory.Faker('product_name')
    price = factory.Faker('random_int', min=0, max=100)


class ProductTestCase(unittest.TestCase):

    def create_product_random(self):
        fake_product = ProductFactory()
        return fake_product

    def test_product_creation(self):
        dragon = Product("red_dragon", 10)
        self.assertEqual("red_dragon", dragon.name)
        self.assertEqual(10, dragon.price)
        with self.assertRaises(AssertionError):
            Product("red_dragon", -10)


class InvoiceLineTestCase(unittest.TestCase):

    def test_invoice_lines_creation(self):
        # Create the invoice Lines
        dragon = Product("red_dragon", 10)

        invoice_lines = [InvoiceLine(dragon, 1)]

        self.assertEqual(invoice_lines[0].amount, 10)


class InvoiceTestCase(unittest.TestCase):

    def setUp(self):
        # Create a full invoice
        dragon = Product("red_dragon", 10)
        unicorn = Product("cute_unicorn", 20)
        cat = Product("lolcat", 5)

        invoice_lines = [InvoiceLine(dragon, 1), InvoiceLine(unicorn, 10), InvoiceLine(cat, 42)]

        self.invoice = Invoice("Mona", invoice_lines)

    def test_product_names(self):

        # We check that the invoice lines are correct. We also check the total amount
        products_names = ["red_dragon", "cute_unicorn", "lolcat"]

        for invoice_line, product_name in itertools.zip_longest(self.invoice.invoice_lines, products_names):
            self.assertEqual(invoice_line.product.name, product_name)

    def test_prices(self):
        # with tva by default
        self.assertEqual(self.invoice.final_price, 504.0)
        # without tva
        amount = sum(invoice_line.amount for invoice_line in self.invoice.invoice_lines)
        self.assertEqual(amount, 420.0)
        # We change the TVA, check that the total amount is correctly calculated
        self.invoice.tva = 1.3
        self.assertEqual(self.invoice.final_price, 546.0)

    def test_number_of_lines(self):

        self.assertEqual(len(self.invoice.invoice_lines), 3)


if __name__ == "__main__":
    unittest.main()
