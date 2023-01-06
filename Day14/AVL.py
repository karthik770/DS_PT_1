import sys

class TreeNode(object):
    def __init__(self, key): #100
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  #  [None|100|None|1]

class AVLTree(object):
    def insert_node(self, root, key): #100
        if not root: #true
            return TreeNode(key) # [None|50|None|1]
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete_node(self, root, key): # entire avl tree , 200 # 150,200 #175,200#180,200#190,200

        if not root: 
            return root
        elif key  < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key: # 200>150 # 200>175 # 200>180 #200>190
            root.right = self.delete_node(root.right, key)  # 175, 200  #180, 200 #190,200 #200,200
        else: # equal 200=200 
            if root.left is None: #true
                temp = root.right  #temp=200
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right) #190
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key) # 200,190
        if root is None:
            return root

    
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root) # -1
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root 
        

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

   
    def getBalance(self, root): # BF = Height l -Helight R
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

  
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent)
            if last:
                print("R----")
                indent += "     "
            else:
                print("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

myTree = AVLTree()
root = None
nums = [100,50,150,25,75,65,85,125,175,190,180,200]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
	        
	# 		 100
	# 		/     \
	#      50      150  
	#   /    \       /  \
	#  25    75   125  175 
    #       /  \        \ 
	# 	 65    85        180 
	# 					 \
	# 					190  BF=0-1=-1
	# 					    \
	# 					    200 



key = 75
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)