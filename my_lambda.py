# lambda arguments: expression
# map (func, seq)
from functools import reduce
add10 = lambda x: x + 10

print(add10(5))

mult = lambda x,y: x*y

print(mult(4,6))

points2D = [(1, 2), (15, -1), (5, -1), (10, 3)]

point2D_sorted = sorted(points2D)
print(points2D)
print(point2D_sorted)

sort_by_y = lambda x: x[1]
point2D_sorted = sorted(points2D, key= sort_by_y)
print(points2D)
print(point2D_sorted)

sort_by_acc = lambda x: x[0] + x[1]
point2D_sorted = sorted(points2D, key= sort_by_acc)
print(points2D)
print(point2D_sorted)

print("\n\nMAP\n___")
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(a)
print(list(b))

c = [x*2 for x in a]
print(c)

print("\n\nFilter\n___")
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(a)
print(list(b))

c = [x for x in a if x%2!=0]
print(c)

print("\n\nReduce\n___")
a = [1, 2, 3, 4, 5, 6]

product_a = reduce(lambda x,y: x*y, a)
print(a)
print(product_a)


