import time as t

class Stack:
    def __init__(self):
        self.list = []

    def empty(self):
        return len(self.list) == 0
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if not self.empty():
            self.list.pop()
        else:
            raise IndexError("A lista está vazia")
        
    def top(self):
        if not self.empty():
            return self.list[-1]
        else:
            return None


stack = Stack()

for i in range(100+1):
    stack.push(i)
    print(f"Lista: {stack.list}\n")
    t.sleep(0.1)

print(f"Lista preenchida: {stack.list}\n")
print("Aguarde...")
t.sleep(3)

while not stack.empty():
    last_item_list = stack.top()
    stack.pop()
    print(f"Item removido da lista com sucesso: {last_item_list}\n")
    print(f"Lista: {stack.list}\n")
    t.sleep(0.1)
