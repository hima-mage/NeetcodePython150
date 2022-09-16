# create empty list
stack = []

# append function to push element into the stack  O(1)
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function is to pop last element in the stack using LIFO O(1)
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)


# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty