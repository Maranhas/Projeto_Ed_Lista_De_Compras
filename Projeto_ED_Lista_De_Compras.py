
class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def remove(self, item):
        if not self.head:
            return
        if self.head.item == item:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.item == item:
                current.next = current.next.next
                return
            current = current.next


class DoubleNode:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        node = DoubleNode(item)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def remove(self, item):
        if not self.head:
            return
        if self.head.item == item:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        current = self.head
        while current.next:
            if current.next.item == item:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                else:
                    self.tail = current
                return
            current = current.next


def binary_search(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


lista_compras = DoubleLinkedList()


def adicionar_item():
    nome = input("Nome do item: ")
    nome.capitalize
    quantidade = int(input("Quantidade: "))
    item = Item(nome, quantidade)
    lista_compras.add(item)
    print("Item adicionado à lista de compras!")

while True:
    print("\n-------- MENU --------")
    print("1. Adicionar item à lista de compras")
    print("2. Mostrar lista de compras")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        adicionar_item()
    elif opcao == 2:
        current = lista_compras.head
        print("Lista de compras:")
        while current:
            print("- {} ({})".format(current.item.nome, current.item.quantidade))
            current = current.next

    elif opcao == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
