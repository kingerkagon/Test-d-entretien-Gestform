import unittest
import random


def create_random_list_test(list_lenght: list):
    """ Permet de créer une liste composé de nombres
    entiers compris entre -1000 et 1000

    Args:
        list_lenght (int): taille de la liste à créer
    return:
        my_liste (list): liste aléatoire
    """
    try:
        my_liste = random.sample(range(-1000, 1000), list_lenght[0])
    except TypeError:
        my_liste = [0]

    return my_liste


def parse_list_data_test(list_to_parse: list):
    """Traite une liste et pour retourner une liste composé
    de chaines de charactère en fonction de la valeur de la liste

    Args:
        list_to_parse (list): liste de nombres entiers aléatoire à traiter

    Returns:
        result_list (list) : liste d'output composé de strings
    """
    result_list = []

    if list_to_parse is None:
        result_list = ["La liste d'entrée est vide"]
    else:
        # Logique de traitement de la liste
        for number in list_to_parse:
            try:
                if (number % 3 == 0 and number % 5 == 0):
                    result_list.append("GestForm")
                elif number % 3 == 0:
                    result_list.append("Gest")
                elif number % 5 == 0:
                    result_list.append("Form")
                else:
                    result_list.append(str(number))
            except TypeError:
                result_list.append("-/-")

    return result_list


class TestRandomList(unittest.TestCase):
    """
    Classe de test sur l'api random_lists
    """

    def test_parsing_data(self):
        """
        Test la capacité de la méthode à traiter les int
        """
        test_data = [5, 3, 6, 8, 4]
        result = parse_list_data_test(test_data)
        self.assertEqual(result, ['Form', 'Gest', 'Gest', '8', '4'])

    def test_exceptions_type(self):
        """
        Test la capacité de la méthode à traiter les cas particuliers de type
        """
        test_data = [5, "5", 6, "8", 4]
        result = parse_list_data_test(test_data)
        self.assertEqual(result, ['Form', "-/-", 'Gest', "-/-", '4'])

    def test_exceptions_length(self):
        """
        Test la capacité de la méthode à traiter les cas particuliers
        de taille de liste
        """
        test_data = []
        result = parse_list_data_test(test_data)
        self.assertEqual(result, [])

    def test_exceptions_none(self):
        """
        Test la capacité de la méthode à traiter le cas où 
        la liste n'existe pas
        """
        test_data = None
        result = parse_list_data_test(test_data)
        self.assertEqual(result, ["La liste d'entrée est vide"])

    def test_creation_random_list(self):
        """
        Test la capacité de la méthode à créer la bonne taille de liste
        """
        test_data = [5]
        result = create_random_list_test(test_data)
        self.assertEqual(len(result), 5)

    def test_creation_type_errror(self):
        """
        Test la capacité de la méthode à créer la bonne taille de liste
        """
        test_data = ["18"]
        result = create_random_list_test(test_data)
        self.assertEqual(result, [0])

    def test_creation_none_error(self):
        """
        Test la capacité de la méthode à créer la bonne taille de liste
        """
        test_data = None
        result = create_random_list_test(test_data)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()
