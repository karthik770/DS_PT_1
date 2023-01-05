class Node:
    def __init__(self, data): # 12
      self.left = None 
      self.right = None
      self.data = data # [None | 12 | None]
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
    def insert(self, data): # 6 # 14 #3   #  [[None | 6| None] | 12 | [None| 14 | None]] 
               
                # 12
                # /\
                # 6 14
                # /
                # 3    
        if self.data:# -->12 0th index or 1st value in node / Root node 
            if data < self.data: # 6<12 -> 6 is less than 12  [None | 12 | None] 14<12
                if self.left is None: 
                    self.left = Node(data) #   [[None | 6| None] | 12 | None]  
                else:
                    self.left.insert(data) 
            elif data > self.data: #14>12 14 is greater than 12
                #   [[None | 6| None] | 12 | None] 
                if self.right is None:
                    self.right = Node(data) #14  [None| 14 | None]
                     #   [[None | 6| None] | 12 | [None| 14 | None]] 

                else:
                    self.right.insert(data)
        else:
            self.data = data

root = Node(12) 
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()