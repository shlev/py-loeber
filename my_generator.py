def generator1():
    yield 1
    yield 2
    yield 3


g = generator1()
print(g)

for i in g:
    print(i)

try:
    print(next(g))
except Exception as e:
    print(f'Catch Exception of type {type(e)}')

g = generator1()
print(next(g))
print(sum(g))


def generator2():
    yield 5
    yield 2
    yield 4


print(sorted(generator2()))

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

print(next(cd))
print(sum(cd))


def firstn(n):
    nums = []
    num=0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstn(10))
print(sum(firstn(10)))

print(sum(firstn_generator(10)))

import sys

print(sys.getsizeof(firstn(10000)))
print(sys.getsizeof(firstn_generator(10000)))

def fibonachi(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
fib = fibonachi(30)
for i in fib:
    print(i)

# generator expression
genExp = (i for i in range(100) if i % 2 == 0)
listExp = [i for i in range(100) if i % 2 == 0]

for i in genExp:
    print(i)

print(sys.getsizeof(genExp))
print(sys.getsizeof(listExp))






