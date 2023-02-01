# from binarytree import Node
# from binarytree import build
# from binarytree import tree
# from binarytree import bst
# root = Node(3)
# root.left = Node(6)
# root.right = Node(8)

# print("binary tree",root)

# print('list of nodes:' ,list(root))

# print('inorder of nodes',root.inorder)

# print('size of the tree', root.size)

# print('height of the tree', root.height)

# print('properties of tree', root.properties)

# #binary tree from the list
# nodes = [3,8,1,4,18,None,14]
# binary_tree = build(nodes)
# print('binary tree', binary_tree)
# print('list from binary tree',binary_tree.values)

# root = tree()
# print("binary tree of any height")
# print(root)

# root2 = tree(height = 2)
# print('binary tree of given height')
# print(root2)

# root3 = tree(height =3, is_perfect=True)
# print('perfect binary tree of given height')
# print(root3)

# #Binary search Tree
# root = bst()

# print('Bst of any height',root)

# root2 = bst(height=2)
# print('bst in given height',root2)

# root3 = bst(height=3, is_perfect=True)
# print('perfect bst in given height',root3)


# #Tail RECURSION
# def rec(n):
#     if n > 0:
#         print(n)
#         rec(n-1)
# rec(10)

# #Head RECURSION
# def rectwo(n):
#     if n>0:
#         print('called')
#         rectwo(n-1)
#         print(n)
# rectwo(10)

#TREE RECURSION
#a function calls itself twice after base condition
# def recThree(n):
#     if n>0:
#         print('called first')
#         recThree(n-1)
#         print(n)
#         print('called second')
#         recThree(n-1)
# recThree(3)

#Indirect recursion

# def calculateA(n):
#     if n>0:
#         print(n,'--A')
#         calculateB(n-1)

# def calculateB(n):
#     if n > 0:
#         print(n,'--B')
#         calculateA(n-1)

# calculateA(4)

#sum of n natural numbers 

# def sum(n):
#     if n== 1:
#         return 1
#     print(n-1,'+++',n)
#     return sum(n-1)+n
# print(sum(10))

# def sum(n):
#     if n== 0:
#         return 0
#     print(n-1,'+++',n)
#     sum(n-1)
#     print('after call')
#     print(n-1,'+++',n)
# print(sum(10))

#factorial of a number
def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n
print(fact(500))