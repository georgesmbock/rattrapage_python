__author__ = 'MBOCK MBOCK Georges Christian'
__license__ = 'Prepa'
__version__ = '0.1.0'
__email__ = 'georgesmbo89@gmail.com'

from collections import UserString

# Creating a Mutable String
class Mystring(UserString):
    """Cette classe hérite de la classe UserString et ajoute deux nouvelles méthodes. head() et tail()

    Args: pas d'attribue particulier sauf celui hérité
    """
    def head(self, n=1):
        """Cette methode affiche les n premiers caractère de la chaine entrée


        Args:
            n (int, optional): nombre des n premiers caractères qu'on souhaite afficher. valeur par de n est 1.

        Returns:
            chaine: la chaine de caractère de longueur n des premiers caractères
        """
        return self.data[:n]
    
    def tail(self, n=1):
        """Cette methode affiche les n derniers caractère de la chaine entrée

        Args:
            n (int, optional): nombre des n derniers caractères qu'on souhaite afficher. valeur par de n est 1.

        Returns:
            chaine: la chaine de caractère de longueur n des derniers caractères de la chiane
        """
        return self.data[-n:]
        
s1 = Mystring("prepa big data")
print(s1.data) # affiche: prepa data
print(s1.head()) # affiche: p
print(s1.head(2)) # affiche: pr
print(s1.tail()) # affiche: a
print(s1.tail(3)) # affiche: ata