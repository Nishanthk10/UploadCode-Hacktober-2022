1. Linear Data Structure:
Linear data structure used to store homogeneous / Non homogeneous elements at contiguous locations.

For example: let us say, we want to store marks of all students in a class, we can use an list to store them. This helps in reducing the use of number of variables as we don’t need to create a separate variable for marks of every students. All marks can be accessed by simply traversing the list



a) List Array
An list array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the list array (generally denoted by the name of the list array).


import array as arr
a1=arr.array("i",[1,2,3,4,5])
a2=arr.array("f",[1.3,0.56,8.9])
a1.append(7)
a1.pop()
print(a1)



import array as arr
a1=arr.array("i",[1,2,3,4,5])
a2=arr.array("f",[1.3,0.56,8.9])
a1.insert(2,56)
print(a1)


i=signed I=unsigned



Operations on Array :

i) append():- This function is used to add the value mentioned in its arguments at the end of the array.

ii) insert(i,x) :- This function is used to add the value(x) at the ith position specified in its argument.

iii) pop():- This function removes the element at the position mentioned in its argument and returns it.

iv) remove():- This function is used to remove the first occurrence of the value mentioned in its arguments.

Time Complexity

Let size of list array be n.

Accessing Time: O(1) [This is possible because elements are stored at contiguous locations]

Search Time: O(n) for Sequential Search: O(log n) for Binary Search [If Array is sorted]

Insertion Time: O(n) [The worst case occurs when insertion happens at the Beginning of an array and requires shifting all of the elements]

Deletion Time: O(n) [The worst case occurs when deletion happens at the Beginning of an array and requires shifting all of the elements]

b) Linked list
A linked list is a linear data structure (like List arrays) where each element is a separate object. Each element (that is node) of a list is comprising of two items – the data and a reference to the next node.

linkedlist.png

Advantages over arrays

Ease of insertion/deletion

Drawbacks:

1) Random access is not allowed.

2) Extra memory space for a pointer is required with each element of the list.

3) Not cache friendly.

Representation:

Operations on linkedlist :

i) Linked List Traversal
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)

l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()





ii) Delete first node
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
  def delfirst(self):
    temp=self.head
    self.head=temp.next
    temp.next=None
node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)

l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()
print()
l1.delfirst()
l1.view()



iii) delete last node
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
  def dellast(self):
    temp=self.head
    while temp.next.next!=None:
      temp=temp.next
    temp.next=None  
node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)

l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()
print()
l1.dellast()
l1.view()
 


iv) delete any node

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
  def delany(self,data):
    temp=self.head
    while(temp.next.data!=data):
      temp=temp.next
    temp.next=temp.next.next
node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)

l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()
print()
l1.delany(6)
l1.view()
 


v) insert node at last

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
  def inlast(self,data):
    n=Node(data)
    temp=self.head
    while(temp.next!=None):
      temp=temp.next
    temp.next=n

node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)

l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()
print()
l1.inlast(2)
l1.view()
 


vi) insert node at first

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
  def infirst(self,data):
    n=Node(data)
    temp=self.head
    self.head=n
    n.next=temp
       
node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)

l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()
print()
l1.infirst(2)
l1.view()
 

vii) insert node before any node
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def view(self):
    temp=self.head
    while(temp!=None):
      print(temp.data,end=" ")
      temp=temp.next
  def inany(self,data,newdata):
    n=Node(newdata)
    temp=self.head
    while(temp.data!=data):
      temp=temp.next
    temp1=temp.next
    temp.next=n
    n.next=temp1    
node1=Node(8)
node2=Node(4)
node3=Node(5)
node4=Node(6)
l1=Linkedlist()
l1.head=node1
node1.next=node2
node2.next=node3
node3.next=node4
l1.view()
print()
l1.inany(4,9)
l1.view()
