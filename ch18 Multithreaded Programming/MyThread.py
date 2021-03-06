__author__ = 'Richard'

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self._func = func
        self._args = args
        self._name = name

    def run(self):
        # print the starting time
        print("Starting", self._name, "at:", ctime())
        self.res = self._func(*self._args)
        # print the ending time
        print(self._name, 'ends at:', ctime())

    def getResult(self):
        return self.res