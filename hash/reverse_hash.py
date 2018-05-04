#!/usr/bin/python3

#Standard library imports
from collections import deque


class HashIt(object):
    """
    Class contains both str_to_hash(question) and hash_to_str(solution) methods.
    """
    def __init__(self):
        self.queue = deque()
        self._allowed_letters = "acdegilmnoprstuw"

    #Question(Definition of hash)
    #def str_to_hash(self, string):
    #    h = 7
    #    for i in range(len(string)):
    #        h = (h*37 + allowed_letters.index(string[i]))
    #    return h

    #Solution
    def hash_to_str(self, hash_value, string_length=7):
        for i in range(string_length):
            index = hash_value%37
            hash_value = int((hash_value-index)/37)
            self.queue.appendleft(self._allowed_letters[index])
        return ''.join(self.queue)

if __name__ == "__main__":
    obj = HashIt()
    print(obj.hash_to_str(680131659347))
