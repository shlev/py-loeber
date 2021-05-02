# Strings: ordered, immutable, test representation

my_string = "hello String"
print(my_string)
my_string = 'hello "String"'
print(my_string)

my_string = '''Multi
Line string'''
print(my_string)

my_string = "Hellow String"
substring = my_string[1:5]
print(my_string[:5])
print(my_string[:])
print(my_string[::2])
print(my_string[::-1])

my_string = '    Hello String    '
print(my_string)
print(my_string.strip())
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith(' '))
print(my_string.endswith('g    '))
print(my_string.find('ll'))
print(my_string.find('y'))
print(my_string.count('l'))
print(my_string.replace('   ', 'oo'))

my_string = 'how are you doing'
print(my_string.split())
print(".".join(my_string.split()))

# %, .format, f-Strings
var = "Tom"
varD = 5
varF = 4.36643
my_string = "the variable is %s %d %.2f" % (var, varD, varF)
print(my_string)

my_string = "the variable is {} {} {:.2f}".format(var, varD, varF)
print(my_string)

my_string = f"the variable is {var} {varD} {varF:.2f}"
print(my_string)

