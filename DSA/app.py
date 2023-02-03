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
# def fact(n):
#     if n == 0:
#         return 1
#     return fact(n-1)*n
# print(fact(500))

#linear search 
# def liner_search(a,k):
#     index = 0
#     while index < len(a):
#         if a[index] == k:
#             return index
#         index+=1
#     return -1
# a = [10,23,1322,4554,10,10]
# print(liner_search(a,100))


#binary serach iterative
# def binary_search(a,k):
#     l = 0
#     cc = 0
#     r = len(a) -1
#     while l<=r:
#         m = (l + r)//2
#         if k == a[m]:
#             return m
#         elif k < a[m]:
#             r = m-1
#         elif k > a[m]:
#             l = m+1
#         cc+=1 
#         print(cc)
#     return "not found"

# a = [1,4,5,6,7,8,10]
# k = 6

# print(binary_search(a,k))

#binary search recursive

# def binary_rec(a,k,l,r):
#     if l > r:
#         return 'not found'
#     else:
#         m = (l+r)//2
#         if k == a[m]:
#             return m
#         elif k < a[m] :
#             return binary_rec(a,k,l,m-1)
#         elif k > a[m] :
#             return binary_rec(a,k,m+1,r)

# a = [1,4,5,6,7,8,10]
# k = 10
# l = 0
# r = len(a)
# print(binary_rec(a,k,l,r))

#selection sort unstable sort
# a = [4,6,2,1,7,0,4,3]
# n = len(a)
# for i in range(n-1):
#     position =i
#     print(a[i])
#     for j in range(i+1,n):
#         print(a[position],'---',a[j])
#         if a[j] < a[position]:
#             position = j
#     temp = a[i]
#     a[i] = a[position]
#     a[position] = temp
#     print(a)


# selection sort with while loop 
# a = [4,6,2,1,7,0,4,3]
# n = len(a)
# print('break')
# i = 0
# while i <n-1:
#     position = i
#     print(a[i])
#     j= i+1
#     while j <n:
#         # print(a[i],'---',a[j])
#         if a[j] < a[position]:
#             position = j
#         j+=1
#         # print(a[position])
#     temp = a[i]
#     a[i] = a[position]
#     a[position] = temp
#     print(a)
#     # print(j)
#     i+=1
# print(a)


# insertion sort stable 
a = [4,6,2,1,7,0,4,3]
a = [1,6,5,7,3,2,1]
n = len(a)
for i in range(1,n):
    cvalue = a[i]
    position = i
    while position > 0 and a[position-1] > cvalue:
        print(a[position],'---',a[position-1],a,i,cvalue)
        a[position] = a[position-1]
        print(a[position],'---',a[position-1],a,i,cvalue)
        position -=1
    a[position] = cvalue
    print(position)
    print(a[position],'===',cvalue,a)
print(a)

