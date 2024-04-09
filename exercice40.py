__author__ = 'MBOCK MBOCK Georges Christian'
__license__ = 'Prepa'
__version__ = '0.1.0'
__email__ = 'georgesmbo89@gmail.com'

import turtle as t

class Rectangle:
    """Cette classe est une classe rectangle qui possède deux attribus.

    Args: longueur et largeur
    """
    def __init__(self, longueur, largeur):
        """Cette methode est le consturcteur(initialiseur) des attribus de la classe


        Args:
            longueur (Float strictement positif)
            largeur (Float strictement positif)
        """
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):
        """Cette methode trace un rectangle
        Args: pas d'arguments
        """
        t.color("gray")
        t.forward(self.longueur)
        t.left(90)
        t.color("black")
        t.forward(self.largeur)
        t.left(90)
        t.color("brown")
        t.forward(self.longueur)
        t.left(90)
        t.color("blue")
        t.forward(self.largeur)
        t.left(90)
        t.done()
        
if __name__=="__main__":    
    mon_rectangle = Rectangle(200, 100)
    mon_rectangle.tracer_figure()
