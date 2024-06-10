# Stack - Python Implementation

This project consists of a simple stack implementation in Python. A stack is a data structure that follows the "Last In, First Out" (LIFO) principle, where the last element added is the first one to be removed.

## Features

- **Push:** Adds an item to the top of the stack.
- **Pop:** Removes the item from the top of the stack, if any.
- **Top:** Returns the item at the top of the stack without removing it.
- **Empty:** Checks if the stack is empty.

## How to Use

1. Instantiate an object of the `Stack` class.
2. Add elements to the stack using the `push(item)` method.
3. Remove elements from the stack using the `pop()` method.
4. Peek at the top element of the stack without removing it using the `top()` method.
5. Check if the stack is empty using the `empty()` method.

## Usage Example

```python
# Declare the class
stack = Stack()

# Fill the list with 100 numbers
for i in range(100+1):
    stack.push(i)
    print(f"List: {stack.list}\n")
    t.sleep(0.1)

print(f"Filled list: {stack.list}\n")
print("Please wait...")
t.sleep(3)

# Emptying the entire list
while not stack.empty():
    last_item_list = stack.top()
    stack.pop()
    print(f"Item successfully removed from the list: {last_item_list}\n")
    print(f"List: {stack.list}\n")
    t.sleep(0.1)
```

This example demonstrates how to fill a stack with numbers from 0 to 100, print the stack, wait for a few seconds, and then remove each element from the stack while printing the resulting stack.

## Installation Requirements

- Python 3.x

## Author

This code was developed by Ageu Felipe Nunes Moraes (myself) as part of a personal project dedicated to strengthening and maturing coding skills. For any questions or suggestions, please contact me at [ageumoraes67@gmail.com](mailto:ageumoraes67@gmail.com).

## Disclaimer

This is a software project developed by an individual and is not affiliated with any other entity.
