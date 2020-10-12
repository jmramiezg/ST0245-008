class Node:
    def __init__(self, data):
        self.data = data        #------------> este es el dato contenido
        self.next = None        #------------> enlace al siguiente elemento de la lista

class SinglyLinkedList:

    def __init__(self, he): 
        self.he = he            #------------> primer elemento de la lista

    def length(self):           #------------> Funcion que mide el tamaño de la lista
        current = self.he       
        if current is not None:
            count = 1
            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = head.he
            head.he = new_node
        else:
            current = head.he
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def reverse(self,n):
        if n>= self.length():
            n = n%self.length()

        j = 1
        while j<=n:
            current = self.he
            while current.next.next is not None:
                current = current.next
            current.next.next = self.he
            self.he = current.next
            current.next = None
            j = j+1

    def lista(self):
        current = head.he
        while current is not None:
            print(current.data,end = '')
            current = current.next
            print()


head = SinglyLinkedList(Node(1))
for j in range (2,6):
    head.insert(j,j-1)

print('La lista inicial es: ')
head.lista()
head.reverse(3)
print("Lista después de ser rotada: ")
head.lista()