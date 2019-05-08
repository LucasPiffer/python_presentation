class PifferException(Exception):
    pass

try:
    1 / 0
except ZeroDivisionError:
    print('Bad idea')

try:
    open('nonexistingfile', 'rb')
except OSError as err:
    print('Not possible to open the file: ' + err.strerror)


def say_hi():
    raise PifferException

try:
    say_hi()
except PifferException as p:
    print('Caught PifferException')
