class Node:
    def __init__(self, item): #12
        self.left = None
        self.right = None
        self.val = item #[None |12| None]

def inorder(root): 
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)


def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')


def preorder(root):
                  #  [left | root| right]
    if root:
        print(str(root.val) + "->", end='')
        preorder(root.left)
        preorder(root.right)

root = Node(12)
root.left = Node(6)
root.right = Node(19)
root.left.left = Node(2)
root.left.right = Node(7)

print("Inorder traversal ")
inorder(root) #[2,6,7,12,19]

print("\nPreorder traversal ")
preorder(root) # [12,6,2,7,19] 

print("\nPostorder traversal ")
postorder(root) #[2,7,6,19,12]