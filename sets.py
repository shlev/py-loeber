# Sets: unordered, mutable, no duplicates

myset = {1,2,3,2,1}
print(myset)

myset = set([2,3,1])
print(myset)

myset.add(4)
myset.add(6)
myset.remove(3) # error if not exist
print(myset)
myset.discard(4) # remove element if exists
myset.clear() # remove all values

myset = {1,2,3,2,1}

myset.pop() # return randon object and removes it.

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(f"diff{diff}")

print(setB.difference(setA))

print(setA.symmetric_difference(setB))

print(primes.issubset(setA))
print(setB.issubset(setA))

print(setA.issuperset(odds))
print(setB.issuperset(setA))

print(setA.isdisjoint(setB))
print(odds.isdisjoint(evens))