import random

a = random.random()
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10) # 10 included
print(a)

a = random.randrange(1, 10) # 10 excluded
print(a)

a = random.normalvariate(0, 1)
print(a)

mylist = list("ABSCDEFG")
print(mylist)

a = random.choice(mylist)
print(a)

a = random.sample(mylist, 5)
print(a)

a = random.choices(mylist, k=5)
print(a)

a = random.shuffle(mylist)
print(mylist)

random.seed(1)
print('seed 1')
print(random.random())
print(random.randint(1,10))

random.seed(2)
print('seed 2')
print(random.random())
print(random.randint(1,10))

random.seed(1)
print('seed 1')
print(random.random())
print(random.randint(1,10))

random.seed(2)
print('seed 2')
print(random.random())
print(random.randint(1,10))


import secrets

print("\n\nSecrets\n\n")

print(secrets.randbelow(10))

print(secrets.randbits(4))

mylist = list("ABCDEFGH")
print(secrets.choice(mylist))

import numpy as np

print("\n\nNumpy - Arrays\n\n")
print(np.random.rand(3))

print(np.random.rand(3, 3))

print(np.random.randint(0, 10, 3))

print(np.random.randint(0, 10, (3,3)))

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

