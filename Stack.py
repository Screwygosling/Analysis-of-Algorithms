from collections import deque

stack = deque()

#elements to be pushed
stack.append(1)
stack.append(2)
stack.append(3)

print("Initial stack")
print(stack)

#popping elements
#LIFO order is followed
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after elements are popped:")
print(stack)