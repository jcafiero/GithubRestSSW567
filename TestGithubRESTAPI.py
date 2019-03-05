#Author: Jennifer Cafiero
#I pledge my honor that I have abided by the Stevens Honor System

import unittest
import requests
from mock import mock, Mock
from GithubRESTAPI import list_github_user_repos

class TestGithubRESTAPI(unittest.TestCase):
    @mock.patch('requests.get')
    def testJcafiero(self, mock_get):
        mock_responses = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        mock_responses[0].json.return_value = [{'name': 'Courses'}, {'name': 'flawless'}, {'name': 'future_shop'}, {'name': 'GithubRestSSW567'}, {'name': 'HackerRank'}, {'name': 'HackerRank2DArray'}, {'name': 'HackPrinceton2016'}, {'name': 'HackRU2018'}, {'name': 'hello-world'}, {'name': 'jcafiero.github.io'}, {'name': 'LargestPalindromeProduct'}, {'name': 'ProjectEuler-59-XOR-Decryption'}, {'name': 'SSW567ClassifyTriangles'}, {'name': 'TriangleSSW567'}]
        mock_responses[1].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 17}]
        mock_responses[2].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 16}]
        mock_responses[3].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 15}]
        mock_responses[4].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 18}]
        mock_responses[5].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 20}]
        mock_responses[6].json.return_value = [{'commit': 2}, {'commit': 2}]
        mock_responses[7].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 30}]
        mock_responses[8].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 28}]
        mock_responses[9].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 4}]
        mock_responses[10].json.return_value = [{'commit': 2}, {'commit': 2}]
        mock_responses[11].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 12}]
        mock_responses[13].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 12}]
        mock_responses[14].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 3}]
        mock_responses[15].json.return_value = [{'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 2}, {'commit': 5}]
        mock_get.side_effect = mock_responses

        self.assertEqual(list_github_user_repos('jcafiero'), [('Courses', 17), ('flawless', 16),  ('future_shop', 15), ('GithubRestSSW567', 18), ('HackerRank',20), ('HackerRank2DArray', 2), ('HackPrinceton2016', 30), ('HackRU2018', 28), ('hello-world', 4), ('jcafiero.github.io', 2), ('LargestPalindromeProduct', 12), ('ProjectEuler-59-XOR-Decryption', 3),('SSW567ClassifyTriangles', 5), ('TriangleSSW567', 5)])

    #britrollo is a github user with 0 repos
    # def testBritrollo(self, mock_get):
    #     mock_responses = [Mock()]
    #     mock_responses[0].json.return_value = []
    #     mock_get.side_effect = mock_responses
    #     self.assertEqual(list_github_user_repos('britrollo'),[])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
