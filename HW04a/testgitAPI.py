import unittest
from gitAPI import getRepoData


class TestGetRepoData(unittest.TestCase):
    # test correct response
    def testExistingUser(self):
        resp = [('amazon-price-tracker', 3), ('bemin-shaker', 24), ('bemin-shaker.github.io', 30), ('Capella', 1), ('CollabHub', 9), ('Complexity', 30), ('COVID-19-Voice-Assistant', 5), ('CS546', 30),
                ('data-structures-algorithms', 11), ('Musicly', 30), ('ReviewMyCourse', 2), ('SSW215', 7), ('SSW315', 13), ('SSW345', 26), ('SSW567', 19), ('StockPriceDataFeed', 3), ('theStuteApp', 2)]
        self.assertEqual(getRepoData(
            "bemin-shaker"), resp)

    # test nonexistant user
    def testNonExistantUser(self):
        self.assertEqual(getRepoData(
            "notauser1234ndnfr4xbc"), "Error: request to retrieve repo data returned an error with status code 404")


if __name__ == '__main__':
    unittest.main()
