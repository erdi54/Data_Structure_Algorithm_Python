
from collections import deque

stack = deque()

# append() function to push

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
stack.append('f')

print("ilk stact:")
print(stack)


# LIFO
print('Stackten Atılan elmanlar:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Stackten elemanlar çıktıktan sonra :')
print(stack)