import unittest
import mod10sha

class Test_TestMod10sha(unittest.TestCase):
    def test_stringToASCII(self):
        self.assertEqual(mod10sha.stringToASCII('ab7'), [9, 7, 9, 8, 7])
    def test_createNewBlock(self):
        self.assertEqual(mod10sha.createNewBlock([1, 1, 6, 1, 0, 1, 1, 2, 0, 1], [1, 6, 0, 1, 2, 3, 4, 5, 6, 7]), [2, 7, 6, 2, 2, 4, 5, 7, 6, 8])
    def test_addBlocks(self):
        self.assertEqual(mod10sha.addBlocks([1, 1, 6, 1, 0, 1, 1, 2, 0, 1], []), [1, 1, 6, 1, 0, 1, 1, 2, 0, 1])
    def test_addTillModOfTen(self):
        self.assertEqual(mod10sha.addTillModOfTen([1, 6]), [1, 6, 0, 1, 2, 3, 4, 5, 6, 7])
    def test_hash(self):
        self.assertEqual(mod10sha.hash('text'), '2762245768')

if __name__ == '__main__':
    unittest.main()