class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None 
            self.length -= 1
            return temp
    
    def prepend(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return True
    
    def pop_first(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            self.length-=1
            return temp
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = temp.next = None
            self.length-=1
            return temp
        
    def get(self, index):
        if index<0 and index>=self.length:
            return None
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                return temp
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
                return temp

        
        