import itertools
class Product:
    """
    This class describes a given Product to buy
    """

    def __init__(self, name, price):
        self.price = price
        self.name = name


class FactureLine:

    def __init__(self, product, quantity=1):
        """
        :param product: ex : android phone!, of Product class
        :param price: in euros
        :param quantity: the items quantity
        """
        self.product = product
        self.quantity = quantity
        self.line_price = product.price*quantity

    def __str__(self):
        return "This is a facture lines"


class Facture:

    def __init__(self, name, facture_lines, tva = 1.2):
        """
        :param name: ex : Mona
        :param facture_lines: list of facture lines
        :param global_amount:
        :param tva:
        """
        self.name = name
        self.facture_lines = facture_lines
        self.global_price = 0
        for i, facture_line in enumerate(self.facture_lines):
            self.global_price += facture_line.line_price

        self.global_price = self.global_price*tva

    def __str__(self):

        my_facture_description = "Nom :" + self.name + "\n"
        for facture_line in self.facture_lines:
            my_facture_description += "\n" + facture_line.product.name + " quantity : "+ str(facture_line.quantity) \
                                      + " price : "+ str(facture_line.line_price)
        return my_facture_description





def build_factures():
    """
    This function creates a facture with wonderful items
    :return:
    """

    # TODO : ceci est moche, utiliser pytest!

    # Mona achète 3 animaux en plastique
    dragon = Product("red_dragon", 10)
    unicorn = Product("cute_unicorn", 20)
    cat = Product("lolcat", 5)

    # Elle en veut plusieurs de chaque pour faire une ferme magique!
    facture_lines = []
    # un seul dragon sinon ils s'entretuent
    facture_lines.append(FactureLine(dragon, 1))
    facture_lines.append(FactureLine(unicorn, 10))
    facture_lines.append(FactureLine(cat, 42))

    global_facture = Facture("Mona", facture_lines)
    print("Voici le cout de la ferme magique : ", global_facture.global_price, "euros seulement!")
    print(global_facture)
    return global_facture

def test_factures(facture):
    """
    We test that a given facture is correctly built
    :return:
    """
    # We check that the facture lines are correct. We also check the total amount
    products_names = ["red_dragon", "cute_unicorn", "lolcat"]

    for facture_line, products_name in zip(facture.facture_lines, products_names):
        assert facture_line.product.name == products_name
    assert facture.global_price == 504.0


if __name__ == "__main__":
    print("enter main")
    my_facture = build_factures()
    test_factures(my_facture)
    # ugly, to be replaced by pytest
    # Tester le montant global, valide quantité, prix, etc...

