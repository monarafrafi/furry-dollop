from dataclasses import dataclass
import itertools

@dataclass
class Product:
    """
    This class describes a given Product to buy
    """
    name: str
    price: float

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

    def __str__(self):
        return "This is a invoice line"


class Invoice:

    # This is a unique number describing each invoice instance
    invoice_number = 0

    def __init__(self, client, invoice_lines, tva=1.2):
        """
        :param name: ex : Mona
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
            my_invoice_description.append(f"{invoice_line.product.name} quantity : {invoice_line.quantity} price : {invoice_line.amount}")
        return '\n'.join(my_invoice_description)



def build_invoice():
    """
    This function creates a invoice with wonderful items
    :return:
    """

    # Mona achète 3 animaux en plastique
    dragon = Product("red_dragon", 10)
    unicorn = Product("cute_unicorn", 20)
    cat = Product("lolcat", 5)

    # Elle en veut plusieurs de chaque pour faire une ferme magique!
    invoice_lines = [InvoiceLine(dragon, 1), InvoiceLine(unicorn, 10), InvoiceLine(cat, 42)]

    invoice = Invoice("Mona", invoice_lines)
    print("Voici le cout de la ferme magique : ", invoice.final_price, "euros seulement!")
    print(invoice)
    return invoice


def test_invoice():
    """
    We test that a given invoice is correctly built
    :return:
    """
    # We create an incoive
    invoice = build_invoice()
    # We check that the invoice lines are correct. We also check the total amount
    products_names = ["red_dragon", "cute_unicorn", "lolcat"]

    for invoice_line, product_name in itertools.zip_longest(invoice.invoice_lines, products_names):
        assert invoice_line.product.name == product_name
    assert invoice.final_price == 504.0

    # We change the TVA, check that the total amount is correctly calculated
    invoice.tva = 1.3
    assert invoice.final_price == 546.0


if __name__ == "__main__":
    test_invoice()


