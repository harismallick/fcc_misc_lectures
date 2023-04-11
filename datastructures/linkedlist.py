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

print(loopedLList)

arrLList = linkedList([1,2,3,4,5])
print(arrLList)

## So far, we looked at the basic constructors to create a linked list of nodes.

## Traversing a linked list ##

# To traverse from the start to the end of a linked list, define the __iter__ function.
# Termination condition: the last node should point to 'None'.
