#Author: Jennifer Cafiero
#I pledge my honor that I have abided by the Stevens Honor System

import unittest
from GithubRESTAPI import list_github_user_repos

class TestGithubRESTAPI(unittest.TestCase):
    def testJcafiero(self):
        self.assertEqual(list_github_user_repos('jcafiero'), [('Courses', 17), ('CS-182', 2), ('flawless', 16), ('FlawlessHacks', 2), ('future_shop', 15), ('GithubRestSSW567',3), ('HackerRank',20), ('HackerRank2DArray', 2), ('HackPrinceton2016', 30), ('HackRU2018', 28), ('hello-world',4), ('hello-world-1',2), ('jcafiero.github.io', 30), ('LargestPalindromeProduct',12),('opencvdrawing',5),('ProjectEuler-59-XOR-Decryption',3),('SSW567ClassifyTriangles',5),('TriangleSSW567',5)])

    #britrollo is a github user with 0 repos 
    def testBritrollo(self):
        self.assertEqual(list_github_user_repos('britrollo'),[])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
