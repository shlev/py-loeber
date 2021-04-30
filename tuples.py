# Tuple: ordered, immutable, allow duplicates elements
mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple1 = "Tup", "Mush", False
print(mytuple1)

not_tuple = ("Test")
print(type(not_tuple))
tuple1 = ("Tuple",)
print(len(tuple1)) # 1
print(f"not tuple -> {not_tuple}  type {type(not_tuple)}\ntuple -> {tuple}  type {type(not_tuple)}\n")

tuple_from_list = tuple(["Max", 28, "Boston"])
print(tuple_from_list)

#destructure
(name, age, city) = mytuple

print(f"name {name} age-{age} city-{city}")