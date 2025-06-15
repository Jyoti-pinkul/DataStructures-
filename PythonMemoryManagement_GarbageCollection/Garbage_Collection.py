
"""

Python uses automatic memory management —
it handles allocation and deallocation of memory so you don't have to manage it manually (like in C/C++).

Key Concepts:
Component	        Purpose
Heap	            All objects and data structures are stored here
Reference Counting	Tracks how many references point to an object
Garbage Collection   (GC)	Cleans up unused objects (especially circular references)
Memory Pools	    Managed by pymalloc for performance
----------------------------------------
Best Practices to Avoid Memory Issues
----------------------------------------
Avoid global variables for large data

Break reference cycles manually when needed

Use context managers (with open(...)) to release file handles

Use generators/yield instead of loading huge data in memory

Explicitly del large objects when done (esp. in long-running scripts)

"""

import sys

a = []
b = a

print(sys.getrefcount(a))  # Usually 3: a, b, and the getrefcount() call
# -- When the reference count drops to 0, the memory is automatically freed.

class Node:
    def __init__(self):
        self.ref = self

n = Node()
print(sys.getrefcount(n))
del n  # Won't be cleaned immediately, forms a cycle
#print(sys.getrefcount(n))

import gc

gc.collect()  # Force a manual garbage collection

print(gc.get_count())  # Returns the number of objects in each generation

#gc.set_debug(gc.DEBUG_LEAK)  # Enable debug output for leaks


import gc

print("Before GC:", gc.get_count())
gc.collect()  # Force garbage collection
print("After GC:", gc.get_count())


import sys

a = [1, 2, 3, 4, 5]
print("Size of list:", sys.getsizeof(a))  # Includes overhead

b = "Hello World"
print("Size of string:", sys.getsizeof(b))

## tracemalloc – Line-by-Line Memory Tracking

import tracemalloc

tracemalloc.start()

a = [i for i in range(100000)]  # Allocates memory

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")

tracemalloc.stop()


import objgraph

class MyClass:
    pass

x = MyClass()
y = MyClass()
x.other = y
y.other = x  # Circular reference

objgraph.show_backrefs([x], filename='circular_ref.png')  # Opens a PNG file
