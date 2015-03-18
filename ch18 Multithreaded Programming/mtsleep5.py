__author__ = 'Richard'

import threading
from time import ctime
from time import sleep

loops = [4,2]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self._func = func
        self._args = args
        self._name = name

    def run(self):
        self.res = self._func(*self._args)

    def getResult(self):
        return self.res

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('end loop', nloop, 'at:', ctime())

def main():
    print('main function starts at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('ALL DONE AT:', ctime())

if __name__ == '__main__':
    main()