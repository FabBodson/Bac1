from collections import deque

my_list = deque([1, 2, 3])


print(my_list)

my_list.appendleft(4)

print(my_list)

my_list.popleft()

print(my_list)
