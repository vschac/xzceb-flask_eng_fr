import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):   

    def test_e2f(self):

        self.assertEqual(english_to_french('Hello'), 'Bonjour')  
        self.assertNotEqual(english_to_french('yes'), 'yes')

    def test_f2e(self): 

        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('oui'), 'oui') 

unittest.main() 