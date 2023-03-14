with open('notes.txt', 'w') as file:
    file.write('Bkk yaar ...')

file = open('notes.txt', 'w')

try:
    file.write('Bkk yaar ...')
finally:
    file.close()



""" ---------------------------------------------------------------------------------------------------------------------- """

from threading import Lock

lock = Lock()

lock.acquire()
#.............
lock.release()

with lock:
    #.............


""" ----------------------------------------------------------------- """

class ManagedFile:
    def __init__(self, filename):
        print('Init')
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
            
        # print('exc : ', exc_type, exc_value)
        print('Exit')
        return True

with ManagedFile('NewNotes.txt') as file:
    file.write('Bkk yaar ...')
    file.write('Bkk yaar ...')
    file.write('Bkk yaar ...')
print('Continuing...')

""" ---------------------------------------------- """

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes2.txt') as file:
    file.write('Bkk yaar ... ')
    file.write('Bkk yaar ... ')
    file.write('Bkk yaar ... ')