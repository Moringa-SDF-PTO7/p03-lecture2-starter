# data_structures.py

# List: A basic data structure in Python
my_list = [1, 2, 3, 4, 5]
print(f"Original List: {my_list}")

# Stack: Last-In-First-Out (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack after pushing elements: {stack}")
stack.pop()
print(f"Stack after popping an element: {stack}")

# Queue: First-In-First-Out (FIFO)
from collections import deque
queue = deque([1, 2, 3])
print(f"Queue: {queue}")
queue.append(4)
queue.popleft()
print(f"Queue after enqueue and dequeue: {queue}")

# TODO: Implement a priority queue using the heapq module
