from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_100(number, lock):
        for i in range(100):
            time.sleep(0.01)
            with lock:
                number.value += 1

if __name__ == "__main__":
    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beginning is: ', shared_number.value)
    
    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('Number at end is: ', shared_number.value)


""" --------------------------------- """

from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_100(numbers, lock):
        for i in range(100):
            time.sleep(0.01)
            for i in range(len(numbers)):
                with lock:
                    numbers[i] += 1

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Number at beginning is: ', shared_array[:])
    
    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print('Number at end is: ', shared_array[:])



""" ---------------------------------------- """

from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import os
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":
    numbers = range(1 ,6)
    q = Queue()
    p1 = Process(target=square, args=(numbers, q))
    
    p2 = Process(target=make_negative, args=(numbers, q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())


""" ---------------------------------------- """

from multiprocessing import Pool

def cube(number):
    return number*number*number

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()
    
    # Map Apply, Join, Close
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])
    
    pool.close()
    pool.join()
    print(result)