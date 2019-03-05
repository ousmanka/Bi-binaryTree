import unittest
from guess import add_Guess


class MyTestCase(unittest.TestCase):

    add_Guess("technology")
    def test_fileIsUpdated(self):
        with open("guess.txt") as file:
            last = file.readlines()[-2]
        self.assertEqual(last, "technology" + "\n")

    add_Guess("bubbles")
    def test_fileIsUpdated2(self):
        with open("guess.txt") as file:
            last = file.readlines()[-1]
        self.assertEqual(last, "bubbles" + "\n")

if __name__ == '__main__':
    unittest.main()
