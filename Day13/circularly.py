class Node:
   def __init__(self, my_data):
      self.data = my_data
      self.next = None # [56| None]

class circularLinkedList:  
   def __init__(self):
      self.head = None
   def add_data(self, my_data): # 56,78,12
      ptr_1 = Node(my_data)  # ptr_1=[12| None] 
      temp = self.head   # [56|head]
      ptr_1.next = self.head  # [56| add of 78 ] ->[78|add of 56]->[12|add of 56]

      if self.head is not None:
         while(temp.next != self.head):
            temp = temp.next
         temp.next = ptr_1  # [56| add of 78 ] ->[78|add of 56]
      else:
         ptr_1.next = ptr_1
      self.head = ptr_1  # [56| add of 78 ] ->[78|add of 12]->[12|add of 56]
   def print_it(self):
      temp = self.head
      if self.head is not None:
         while(True):
            print("%d" %(temp.data)),
            temp = temp.next
            if (temp == self.head):
               break

my_list = circularLinkedList() 
print("Elements are added to the list ")
my_list.add_data (56)
my_list.add_data (78)
my_list.add_data (12)
print("The data is : ")
my_list.print_it()