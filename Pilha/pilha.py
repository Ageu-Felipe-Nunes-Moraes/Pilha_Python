import time as t

class Pilha:
    def __init__(self):
        self.lista = []

    def vazia(self):
        return len(self.lista) == 0
    
    def push(self, item):
        self.lista.append(item)
    
    def pop(self):
        if not self.vazia():
            self.lista.pop()
        else:
            raise IndexError("A lista está vazia")
        
    def topo(self):
        if not self.vazia():
            return self.lista[-1]
        else:
            return None


pilha = Pilha()

for i in range(100+1):
    pilha.push(i)
    print(f"Lista: {pilha.lista}\n")
    t.sleep(0.1)

print(f"Lista preenchida: {pilha.lista}\n")
print("Aguarde...")
t.sleep(3)

while not pilha.vazia():
    ultimo_item_lista = pilha.topo()
    pilha.pop()
    print(f"Item removido da lista com sucesso: {ultimo_item_lista}\n")
    print(f"Lista: {pilha.lista}\n")
    t.sleep(0.1)
