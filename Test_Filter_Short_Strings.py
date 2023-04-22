from Filter_Short_Strings import long
import unittest


class TestFilterStrings(unittest.TestCase):
    def test_filter_strings(self):
        # Test avec une liste de chaînes vide
        self.assertEqual(long([], 5), [])

        # Test avec une liste de chaînes avec des chaînes plus courtes que la longueur minimale
        self.assertEqual(long(['abc', 'def', 'ghi'], 4), [])

        # Test avec une liste de chaînes avec des chaînes plus longues que la longueur minimale
        self.assertEqual(long(['abcdef', 'ghijkl', 'mnopqr'], 5), ['abcdef', 'ghijkl', 'mnopqr'])

if __name__ == '__main__':
    unittest.main()
