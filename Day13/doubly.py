
class Node:
    def __init__(self, value): #[None| 5 | None]
        self.previous = None
        self.data = value
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def insertAtBeginning(self, value): #5
        new_node = Node(value) # new_node=[None|5|None]
        if self.isEmpty():
            self.head = new_node # self.head= [None|5|None]
        else: # --> There is many value in linkedlist
            new_node.next = self.head #  [None|5|address of 3]-> [address of 5|3|next] ->[prev|6|None]
            self.head.previous = new_node 
            self.head = new_node  # [None|5|address of 3] --> Head

    def insertAtEnd(self, value): #[None|5|None] -> [|10|None]
        new_node = Node(value)  #[None|10|None]
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head  #[None|5|None] -> [None|10|None]
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node #[None|5|address of 10] -> [address of 5|10|None]
            new_node.previous = temp 

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, sep=",")
            temp = temp.next

    def delete(self, value): #100
        if self.isEmpty(): #true
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None: #[None|100|None] 
            if self.head.data == value: #100 ==100
                self.head = None #--> deletion
        else: #[None|1|add of 5], [add of 1|5|add of 10],[add of 5|10|add of 25],25,100
            temp = self.head #[None|1|add of 5]
            while temp is not None: #[add of 25|100|None]
                if temp.data == value: #100==100 true
                    break
                temp = temp.next
            if temp is None:
                print("Element not present in linked list. Cannot delete element.")
            elif temp.next is None:
                 temp=None
            else:
                temp.next = temp.previous.next
                temp.next.previous = temp.previous
                temp.next = None
                temp.previous = None

x = DoublyLinkedList()
# print(x.isEmpty())
x.insertAtBeginning(5)
x.insertAtEnd(10)
x.insertAtEnd(25)
x.insertAtEnd(100)
x.insertAtBeginning(1)
x.printLinkedList()
x.delete(100)
#1, 5,10,25,100