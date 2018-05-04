#!/usr/bin/python3

#Standard libraby import
import unittest

#Local imports
from crawl import CrawlIt

class TestQuery(unittest.TestCase):

    #Test for query one
    def test_query_one(self):
        obj = CrawlIt()
        test_kw = "subtle_art_of_not_giving_a"
        res = obj.query_one(test_kw)
        self.assertEqual(res, 81)

    #Test for query two
    def test_query_two(self):
        obj = CrawlIt()
        test_kw = "subtle_art_of_not_giving_a"
        test_page_number = 3
        res = obj.query_two(test_kw, test_page_number)
        self.assertEqual(len(res), 1)

    #Test for query two when no result found on page
    def test_query_two_no_result(self):
        obj = CrawlIt()
        test_kw = "subtle_art_of_not_giving_a"
        test_page_number = 100
        res = obj.query_two(test_kw, test_page_number)
        self.assertEqual(res, 0)



if __name__ == "__main__":
    unittest.main()
