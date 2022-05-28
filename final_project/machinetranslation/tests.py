import unittest
from translator import english_to_french,french_to_english

class test_english_to_french(unittest.TestCase): 
    def null_test(self): 
        self.assertEqual(english_to_french(" "), " ")
    def translate_test(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class test_french_to_english(unittest.TestCase): 
    def null_test(self): 
        self.assertEqual(french_to_english(" "), " ")
    def translate_test(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()