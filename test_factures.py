import unittest
from factures import Product, InvoiceLine, Invoice
import itertools


class ProductTestCase(unittest.TestCase):

    def test_product_creation(self):
        dragon = Product("red_dragon", 10)
        self.assertEqual("red_dragon", dragon.name)
        self.assertEqual(10, dragon.price)
        with self.assertRaises(AssertionError):
            fakedragon = Product("red_dragon", -10)


class InvoiceLineTestCase(unittest.TestCase):

    def test_invoice_lines_creation(self):
        # Create the invoice Lines
        dragon = Product("red_dragon", 10)

        invoice_lines = [InvoiceLine(dragon, 1)]

        self.assertEqual(invoice_lines[0].amount, 10)


class InvoiceTestCase(unittest.TestCase):

    def test_invoice_creation(self):
        # Create a full invoice
        dragon = Product("red_dragon", 10)
        unicorn = Product("cute_unicorn", 20)
        cat = Product("lolcat", 5)

        invoice_lines = [InvoiceLine(dragon, 1), InvoiceLine(unicorn, 10), InvoiceLine(cat, 42)]

        invoice = Invoice("Mona", invoice_lines)
        # We check that the invoice lines are correct. We also check the total amount
        products_names = ["red_dragon", "cute_unicorn", "lolcat"]

        for invoice_line, product_name in itertools.zip_longest(invoice.invoice_lines, products_names):
            self.assertEqual(invoice_line.product.name, product_name)
        self.assertEqual(invoice.final_price, 504.0)

        # We change the TVA, check that the total amount is correctly calculated
        invoice.tva = 1.3
        self.assertEqual(invoice.final_price, 546.0)


if __name__ == "__main__":
    unittest.main()