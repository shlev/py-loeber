# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, "apple", "apple", "pop"]
print(mylist3)

item = mylist3[1]
print(item)

item1 = mylist3[-1]
print(item1)

for x in mylist3:
    print(x)

if "pop" in mylist3:
    print("yes")
else:
    print("no")

print(len(mylist3))

mylist3.append("tut")
print(mylist3)

mylist3.insert(1, "blueberry")
print(mylist3)

pop_item = mylist3.pop()
print(f"item {pop_item} updated list: {mylist3}")
mylist3.remove("apple")
print(mylist3)

mylist3.reverse()
print(mylist3)

# mylist3.sort()
# new_list = sorted(mylist3)

list_of_zero = [0] * 5
print(list_of_zero)

list_count = [1, 2, 3, 4, 5]
print(list_count + list_of_zero)


print(list_count[2:4])

list_cpy = list_count[:]
print(list_cpy)

list_sqr = [x*x for x in list_cpy]
print(list_sqr)
