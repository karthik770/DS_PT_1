class Node:
    def __init__(self, item): #(self,1)
        self.item = item  #[1|None]
        self.next = None 
       
class LinkedList:
    def __init__(self):
        self.head = None
        # Head [1|address of 2]--> [2|none] tail

linked_list = LinkedList() # Head ->None
linked_list.head = Node(1)  # linked_list.head =[1|None]
second = Node(2)  # second =[2|None]
third = Node(3)  # third =[3|None]
# linked_list.head =[1|next=None] 
linked_list.head.next = second   # linked_list.head =[1|[2|None]]
second.next = third  #second [2|[3|None]]

#1|second  --> 2|third ---> 3| none

while linked_list.head != None:
    print(linked_list.head.item, end=" ")
    linked_list.head = linked_list.head.next
