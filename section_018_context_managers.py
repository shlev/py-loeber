# used to manage resources
# will correctly close notes.txt when finished or an exception is raised.
with open('notes.txt', 'w') as file:
    file.write('some to do....')

# above code is cleaner than the next one which does the same

file = open('notes.txt', 'w')
try:
    file.write('some todo...')
finally:
    file.close()

# thread as resource
from threading import Lock
lock = Lock()

lock.acquire()
#... some code
lock.release()

#auto acquire and release
with lock:
    # ....some code


# implements context manager to class


class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    # runs as we allocate resource
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled:')
        print('exit')
        return True


with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('some todo...')

print('continuing')


# context manager to function

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

# use managed function
with open_managed_file('notes_txt') as f:
    f.write('some todooo from managed function....')
