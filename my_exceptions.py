# Errors and Exceptions

#NameError
#ValueError
#IndexError
#ImportError
#KeyError

def raiseException():
    x = -5
    if x < 0:
        raise Exception('x should be positive')

def assertExample():
    x = -4
    assert(x>=0), 'x is not positive'

try:
    raiseException()
except Exception as e:
    print("an error happend")
    print(e)

# assertExample()

try:
    a = 5 / 0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)
try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)



