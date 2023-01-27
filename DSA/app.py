from binarytree import Node
from binarytree import build
from binarytree import tree
from binarytree import bst
root = Node(3)
root.left = Node(6)
root.right = Node(8)

print("binary tree",root)

print('list of nodes:' ,list(root))

print('inorder of nodes',root.inorder)

print('size of the tree', root.size)

print('height of the tree', root.height)

print('properties of tree', root.properties)

#binary tree from the list
nodes = [3,8,1,4,18,None,14]
binary_tree = build(nodes)
print('binary tree', binary_tree)
print('list from binary tree',binary_tree.values)

root = tree()
print("binary tree of any height")
print(root)

root2 = tree(height = 2)
print('binary tree of given height')
print(root2)

root3 = tree(height =3, is_perfect=True)
print('perfect binary tree of given height')
print(root3)

#Binary search Tree
root = bst()

print('Bst of any height',root)

root2 = bst(height=2)
print('bst in given height',root2)

root3 = bst(height=3, is_perfect=True)
print('perfect bst in given height',root3)