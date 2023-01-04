from binarytree import *
root = Node(3)
root.left = Node(6)
root.right = Node(8)
print('Binary tree :', root)
print('List of nodes :', list(root))
print('Size of tree :', root.size)
print('Height of tree :', root.height)
print('Properties of tree : \n', root.properties)


# from binarytree import build
# nodes =[3,4,5,6,7,8,9]
# bt=build(nodes)
# print(bt)