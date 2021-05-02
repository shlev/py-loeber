# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
a = "aaaaabbbcccccc"
my_counter = Counter(a)
print(f"{my_counter} {type(my_counter)}")
print(my_counter.most_common(2))
print(list(my_counter.elements()))

# namedtuple

print('namedtuple')
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)

# OrderedDict

print('OrderedDict')

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['b'] = 2

print(ordered_dict)

# defaultDict return default value if key not exist
print('defaultdict')

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque

print('deque')
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([7,8,9])
print(d)
d.rotate(2)
print(d)






