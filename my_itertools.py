# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators.

from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement, accumulate, groupby
from itertools import count, cycle, repeat
import operator

# product
print('product\n---------')
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(prod)
print(list(prod))

b = [5]
prod = product(a, b, repeat=2)
print(list(prod))

print('permutation\n---------')

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm = permutations(a, 2)
print(list(perm))

print('combinations\n---------')

a = [1, 2, 3, 4]
comb = combinations(a,2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

print('accumulate\n---------')

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

print('groupby\n---------')

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))

group_obj = groupby(a, key=lambda x: x < 3)

for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# infinite iterators
print("infinite iterators")
print("count")
for i in count(10):
    print(i)
    if i == 15:
        break;

print('cycle')
a = [1, 2, 3]
stop_at = 1
for i in cycle(a):
    print(i)
    stop_at+=1
    if stop_at > 20:
        break

print("repeat")
for i in repeat(1,6):
    print(i)




