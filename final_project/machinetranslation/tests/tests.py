import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french(None),None) # Test for null input for englishToFrench        
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')  # test when 'Hello' is given as input the output is not 'Au revoir'


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None),None) # Test for null input for frenchToEnglish
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello') # test when 'Au revoir' is given as input the output is not 'Hello'       


unittest.main()