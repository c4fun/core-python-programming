from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2kj'] = 345
    d[3.3] = 5.5
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=f, args=(d,l))
        p.start()
        p.join()

        # the d is returned to d because he is a manager type.
        print(d)
        print(l)