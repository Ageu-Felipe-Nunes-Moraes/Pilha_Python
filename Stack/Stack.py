import time as t # Time Method

# Class for stacks operations
class Stack:
    # Initial function
    def __init__(self):
        self.list = []

    # Function that checks if it is empty
    def empty(self):
        return len(self.list) == 0
    
     # Puts item in the final list
    def push(self, item):
        self.list.append(item)
    
     # Removes the last item from the list
    def pop(self):
        # Only delete the item from the list if it is not empty
        if not self.empty():
            self.list.pop()
        else:
            raise IndexError("A lista está vazia")
        
    #  Stores the last item in the list in a variable
    def top(self):
        # Return a value only if the list is different from empty
        if not self.empty():
            return self.list[-1]
        else:
            return None

# Declare of the class
stack = Stack()

# Fills the list with 100 numbers
for i in range(100+1):
    stack.push(i)
    print(f"Lista: {stack.list}\n")
    t.sleep(0.1)

print(f"Lista preenchida: {stack.list}\n")
print("Aguarde...")
t.sleep(3)

# Emptying the entire list
while not stack.empty():
    last_item_list = stack.top()
    stack.pop()
    print(f"Item removido da lista com sucesso: {last_item_list}\n")
    print(f"Lista: {stack.list}\n")
    t.sleep(0.1)
