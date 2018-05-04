#!/usr/bin/python3

#Standard library import(s)
import unittest

#Local import(s)
from reverse_hash import HashIt


class TestHashMethod(unittest.TestCase):
    """
    Basic test class to test the hash_to_str method
    """
    def test_hash_to_str(self):
        obj = HashIt()
        result = obj.hash_to_str(680131659347, 7)
        self.assertEqual(result, 'leepadg')

if __name__ == '__main__':
    unittest.main()
