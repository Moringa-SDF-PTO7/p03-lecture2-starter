# data structure => form/means/way for storing data in a computer program.

# Speak of structures that are common and are native (standard library) in python

# 1. list
scores = [ 90, 88, 72, 10 ]
print(f"Scores list {scores}")

# 2. stack => LIFO (Last In - First Out)
stack = []
stack.append(20) # Add item to end of list
stack.append(23)
stack.append(99)
stack.append(1)
print(f"Current stack {stack}")
stack.pop() # with default value => removes the very last index
print(f"Popped stack {stack}")

# 3. queue => FIFO (First In - First Out)
queue = []
queue.append(20) # Add item to end of list
queue.append(23)
queue.append(99)
queue.append(1)
print(f"Current queue {queue}")
queue.pop(0) # with value = 0 => removes the very first index
print(f"Popped queue {queue}")

from collections import deque
curr_queue = deque([90, 91, 92, 93, 94])
print(f"queue {curr_queue}")
curr_queue.append(95)
print(f"queue {curr_queue}")
curr_queue.popleft() # remove item at the start of the queue
print(f"queue {curr_queue}")

# TODO: Implement a `priority` queue using the heapq module