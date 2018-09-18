from dataclasses import dataclass
import unittest
import itertools


class Product:
    """
    This class describes a given Product to buy
    """
    def __init__(self, name, price):
        # The price must be positive
        assert price > 0
        # string and not empty (or spaces only)
        assert isinstance(name, str) and len(name.strip()) > 0
        self.name = name
        self.price = price

@dataclass
class InvoiceLine:
    """
    This class describes a given line of an Invoice
    """

    product: Product
    quantity: int = 1

    @property
    def amount(self):
        """
        :return: the price of one invoice line in euros
        """
        return self.product.price*self.quantity


class Invoice:

    # This is a unique number describing each invoice instance
    invoice_number = 0

    def __init__(self, client, invoice_lines, tva=1.2):
        """
        :param client: ex : Mona
        :param invoice_lines: a list of invoice lines
        :param tva:
        """
        self.client = client
        self.invoice_lines = invoice_lines
        self.tva = tva
        Invoice.invoice_number += 1

    @property
    def final_price(self):
        """
        This property calculates the final price of the invoice, TVA included
        :return: the final price
        """
        return sum(invoice_line.amount for invoice_line in self.invoice_lines)*self.tva

    def __str__(self):

        my_invoice_description = [f"Number : {Invoice.invoice_number} Client: {self.client}"]
        for invoice_line in self.invoice_lines:
            my_invoice_description.append(f"{invoice_line.product.name} "
                                          f"quantity : {invoice_line.quantity} price : {invoice_line.amount}")
        return '\n'.join(my_invoice_description)

