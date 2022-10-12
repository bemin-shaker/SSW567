import unittest
from unittest import mock
from gitAPI import getRepoData


class TestGetRepoData(unittest.TestCase):
    @mock.patch("gitAPI.getRepoData", return_value=[('amazon-price-tracker', 3), ('bemin-shaker', 24), ('bemin-shaker.github.io', 30), ('Capella', 1), ('CollabHub', 9), ('Complexity', 30), ('COVID-19-Voice-Assistant', 5), ('CS546', 30),
                                                    ('data-structures-algorithms', 11), ('Musicly', 30), ('ReviewMyCourse', 2), ('SSW215', 7), ('SSW315', 13), ('SSW345', 26), ('SSW567', 20), ('StockPriceDataFeed', 3), ('theStuteApp', 2)])
    # test correct response
    def testExistingUser(self, mockGetRepoData):
        resp = [('amazon-price-tracker', 3), ('bemin-shaker', 24), ('bemin-shaker.github.io', 30), ('Capella', 1), ('CollabHub', 9), ('Complexity', 30), ('COVID-19-Voice-Assistant', 5), ('CS546', 30),
                ('data-structures-algorithms', 11), ('Musicly', 30), ('ReviewMyCourse', 2), ('SSW215', 7), ('SSW315', 13), ('SSW345', 26), ('SSW567', 20), ('StockPriceDataFeed', 3), ('theStuteApp', 2)]

        self.assertEqual(mockGetRepoData(
            "bemin-shaker"), resp)

    @mock.patch("gitAPI.getRepoData", return_value="Error: request to retrieve repo data returned an error with status code 404")
    # test nonexistant user
    def testNonExistantUser(self, mockGetRepoData):
        self.assertEqual(getRepoData(
            "notauser1234ndnfr4xbc"), "Error: request to retrieve repo data returned an error with status code 404")


if __name__ == '__main__':
    unittest.main()
