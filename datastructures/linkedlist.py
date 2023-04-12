# Source: https://realpython.com/linked-lists-python/
# Make two classes for creating a singly linked list
# One class to instantiate a node, with data and a pointer to the next node.
# The second class to instantiate the list to link the nodes together.
# If its the first node, it will be the head.
# The last node needs to point to 'null'

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


class linkedList():
    def __init__(self, nodes=None):
        """
        Initiate a new instance of linked list with a list of elements to be instantiated with the Node() class.
        """
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for item in nodes:
                node.next = Node(item)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")
        return "->".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def getData(self):
        """
        Iterate through the linked list to output the data stored in the nodes
        """
        node = self.head
        linkedListData = []
        while node is not None:
            # yield node.data
            linkedListData.append(node.data)
            node = node.next

        return linkedListData

    def addFirst(self, newNode):
        """
        The newNode element is an intance of the Node() class
        """
        newNode.next = self.head
        self.head = newNode

    def addLast(self, newNode):
        """
        The newNode element is an instance of the Node() class and will be added to the end of the linked list.
        """
        if self.head is None:
            self.head = newNode
            return
        
        previousNode = self.head
        while previousNode is not None:
            previousNode = previousNode.next
            if previousNode.next is None:
                previousNode.next = newNode
                return

    def addBefore(self, existingNode, newNode):
        """
        The newNode will be added before the existingNode passed as an argument.
        """
        if self.head is None:
            raise Exception("The list is empty")
        
        if self.head == existingNode:
            return self.addFirst(newNode)
        
        previousNode = self.head
        # while True:
        for node in self:
            if node.data == existingNode:
                previousNode.next = newNode
                newNode.next = node
                return "Node added"
            # print(currentNode)
            previousNode = node

        return "Didn't work"

    def addAfter(self, newNode, existingNode):
        if self.head is None:
            raise Exception("This list is empty")
        
        if self.head == existingNode:
            return self.addLast(newNode)
        
        for node in self:
            if node.data == existingNode:
                temp = node.next
                node.next = newNode
                newNode.next = temp
                return "Node added"
            
    def deleteNode(self, nodeData):
        if self.head is None:
            raise Exception("This list is empty")
        
        # Edge case for the node to be deleted being the head
        if self.head.data == nodeData:
            self.head = self.head.next
            return "Node head changed"
        
        previousNode = self.head
        for node in self:
            if node.data == nodeData:
                previousNode.next = node.next
                return f"{nodeData} deleted"

            previousNode = node

        

    
## Test cases:

l_list = linkedList()

first_node = Node("a")
l_list.head = first_node

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node

print(l_list)

loopedLList = linkedList()

elements = [1,2,3,4,5,6]

previousNode = None
for item in elements:
    node = Node(str(item))

    if loopedLList.head is not None:
        previousNode.next = node
        previousNode = node

    else:
        loopedLList.head = node
        previousNode = node

print(f"Looped list output: {loopedLList}")

arrLList = linkedList([1,2,3,4,5])
print(arrLList)

# Print the data stored in the linked list with the getData() function:

testOutput = arrLList.getData()
print(testOutput)

## So far, we looked at the basic constructors to create a linked list of nodes.

## Traversing (iterating) a linked list ##

# To traverse from the start to the end of a linked list, define the __iter__ function.
# Termination condition: the last node should point to 'None'.

# Adding elements to the linked list #

# There are three different scenarios for adding new nodes to a linked list:
#   - Adding to the beginning of the list (creating a new head)
#   - Adding to the end of the list (existing last node will now point to new node and new node points to null)
#   - Adding to the middle of the linked list. This is involve changing the pointers for the existing elements in the list, to-and-from the new node that will be added.

# Testing the addFirst and AddLast methods of class:

arrLList.addFirst(Node(0))
arrLList.addLast(Node(6))

print(f"Linked list with added elements: {arrLList}")

arrLList.addBefore(5, Node(25))
print(f"Adding new element before specific element in linked list:\n{arrLList}")

arrLList.addAfter(Node(50), 5)
print(f"Element added after the given Node:\n{arrLList}")

# Testing deleting a node with the deleteNode() function #

arrLList.deleteNode(50)
print(f"Array after a node has been deleted:\n{arrLList}")

### Miscellaneous python knowledge for creating linked lists ###

# Understanding the iterators, generators and yield to better understand __iter__ function.
# Iterable - It is any data structure or data type where the stored elements can be read one-by-one, ie, iterated over. Lists, strings, dicts are all iterables.
# Generator - These are a type of iterable where you only iterate over once.
# A generator is created by using () --> see example
# Creating a generator variable, and calling it will not execute the lines of code.
# Only when for .. in ..: iterator syntax is used will the generator code be executed.

# testList = [x*x for x in range(3)]
# testGenerator = (x*x for x in range(3))

# print(testList)
# print(testGenerator)
# #printing the output, we can see that in list comprehension, the elements were stored in memory. For large lists, this can become inefficient.
# # The generator points to an iterable object in memory, but not the actual values, as they have not been computed yet.

# for _ in testGenerator:
#     print(_) # Now the code for the generator comprehension is actually executed.

# def generatorTest():
#     testList = [1,2,3]
#     yield testList[0]
#     yield testList[1]
#     yield testList[2]


# firstGen = generatorTest()
# print(firstGen)
# print(next(firstGen))
# print(next(firstGen))
# print(next(firstGen))

# # the yield keyword returns a generator object, which will point to the objext in memory.
# # To iterate manually through the elements in the generator, need to use the 'next()' method.
# # This can be simplified by using loops:

# def generatorTest2():
#     testList = [4,5,6]
#     for item in testList:
#         yield item

# def genOutput():
#     secondGen = generatorTest2()
#     print(secondGen)

#     for item in secondGen:
#         print(item)

# genOutput()

# def yieldFrom():
#     yield from (x for x in range(3)) # generator within a generator

# def yieldFromOutput():
#     x = yieldFrom()
#     # print(x)
#     for item in x:
#         print(item)

# yieldFromOutput()