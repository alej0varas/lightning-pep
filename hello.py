import time

import os, path


class Felicitations(object):
    def __init__(self): 
        self.felicitations = [ ]

    def addon(self,word):
        self.felicitations.append(word)

    def printme(self):
        greeting = string.join(self.felicitations[0:], "")
        print greeting # Comment

class Empty:
    pass

result = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10+1
