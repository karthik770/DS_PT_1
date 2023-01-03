class Node:
    def __init__(self, item): #(self,1)
        self.item = item  #[1|None]
        self.next = None 
       
class LinkedList:
    def __init__(self):
        self.head = None

        # Head [1|address of 2]--> [2|none] tail
   
linked_list = LinkedList() # Head ->None
linked_list.head = Node(4)  # linked_list.head =[1|None]
second = Node(6)  # second =[2|None]
third = Node(7)  # third =[3|None]
fourth= Node(8)
fifth= Node(9)
sixth=Node(10)
seventh=Node(1)
eigth=Node(2)
ninth=Node(3)
linked_list.head.next = second   # linked_list.head =[1|[2|None]]
second.next = third  #second [2|[3|None]]
third.next=fourth
fourth.next=fifth
fifth.next=sixth
sixth.next=seventh
seventh.next=eigth
eigth.next=ninth # [3 | None]

while linked_list.head != None:
        print(linked_list.head.item ,linked_list.head.next, end=" ")
        linked_list.head = linked_list.head.next
