import unittest
from username import add_username, delete_username


class MyTestCase(unittest.TestCase):
    add_username("4pics1wordPlayaa")
    def test_fileIsUpdated(self):
        answer = False
        with open("username.txt", "r") as file:
            for line in file:
                if line == "4pics1wordPlayaa" + "\n":
                    answer = True
        answer
        self.assertEqual(answer, True, "first add")

    add_username("sillybunny")
    delete_username("sillybunny")
    def test_userGone(self):
        answer = True
        with open("username.txt", "r") as file:
            for line in file:
                if line == "sillybunny":
                    answer = False
        answer
        self.assertEqual(answer, True)

if __name__ == '__main__':
    unittest.main()