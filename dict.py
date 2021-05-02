# Dictionary: Key-Value pairs, unordered, Mutable

mydict = { 'name': 'Max', 'age': 28, 'city': 'New York'}
print(mydict)

mydict2 = dict(name='Mary', age=27, city='Boston')
print(mydict2)

value = mydict['name'] # error if key not exist
print(value)

# add key, overirde old key
mydict['email'] = "max@xyz.com"

print(mydict)

del (mydict['name'])
print(mydict)

mydict.pop('age')
print(mydict)
mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict['name'])

try:
    print(mydict['name'])
except:
    print("error")

for key in mydict2:
    print(key)

for key in mydict.keys():
    print(key)

for value in mydict2.values():
    print(value)

for key,value in mydict2.items():
    print(key, value)

mydict2_cpy = mydict2 # same object, delete item will effect both

mydict2_dup = mydict.copy() #diffrent object

mydict2_dict = dict(mydict2) #diffrent object

#merge dict
my_dict = {'name': 'Max', 'age': 28, 'email': 'max@xyz.com'}
my_dict_2 = {'name': 'Mary', 'age': 27, 'city': 'Boston'}
merge_dict = my_dict.update(my_dict_2)
print(f"{my_dict}\n{my_dict_2}\n{merge_dict}")