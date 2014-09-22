from sprBloom import sprBloom
from sprBloom import *

f1 = sprBloom('test', 1000000, 0.001, sprBloom.SMALL_SET_GROWTH)
#f2 = pyreBloom('fuck', 100, 0.01)
print f1.capacity
#print f2.capacity
for i in range(1, 2000):
    f1.add(str(i))
print f1.capacity
print f1.count
print [str(i) in f1 for i in range(1, 3000)]
