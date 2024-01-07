## Tutorial source: https://www.youtube.com/watch?v=qp8u-frRAnU

## Notes ##
'''
The problem with static arrays: the size of the array must be predetermined and
the size cannot be increased. A new static array must be created if larger arr
capacity is desired.

Dynamic arrays:
- All arrays in Python are dynamic arrays.
- Dynamic arrays in Python automatically increase their capacity when more items
need to be added. This is done by copying the existing array to a new memory
location, and copying the values from the old memory location to the new location
first. The number is new memory address location allotted to the new array is n*2,
where n was the size of the previous array. THEN, new array elements can be added.
- This makes dynamic arrays inefficient in terms of IO operations. If an element
had to be inserted to or deleted from the middle of an array, the memory address
of items succeeding it must be changed.

- This is only an issue because arrays store data in contiguous memory locations!
- While this quality is desirable for certain applications, its not ideal for
others. Another data structure might be better suited.

Linked lists help solve this issue.
With linked lists:
- Python doesn't have to pre-allocate space in memory for the data.
- Insertion operation are easier.
- Insertion operations have O(1) TC for inserting at the start of the list.
- Most LL operations are O(n).
- Arrays are faster at indexing.
'''

## Creating a linked list ##
## Two classes are needed:
# One class to instantiate a node
# One class to link the nodes together

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)
    
    def node_value(self):
        return self.data
    
class LinkedList():
    def __init__(self, nodes: list=None) -> None:
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for item in nodes:
                node.next = Node(item)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")
        return "->".join(nodes)
    
    def get_length(self)-> int:
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count
    
    def add_node(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        node = self.head
        new_node = Node(data)

        if index == 0:
            new_node.next = node
            self.head = new_node
            return "New head created"

        previous_node = None
        i = 0
        while i <= index:
            if i == index:
                previous_node.next = new_node
                new_node.next = node
                break
            previous_node = node
            node = node.next
            i += 1

        return f"{data} added at position {index}"
    
    # def get_smaller_head(self, l2):
    #     self_head = self.head
    #     if self_head.node_value() <= l2.head.node_value():
    #         return self.head
    #     return  l2.head
    

    def combine_sorted_lists(self, list2):
        linked_list_check = isinstance(list2, LinkedList)
        if not linked_list_check:
            raise Exception("Given list is not a linked list")
        
        current_node = self.head
        previous_node = None

        while list2.head is not None:
            node_to_add = list2.head
            new_l2_head = list2.head.next
            # print(current_node)
            # if self.head.node_value() > list2.head.node_value():
            if list2.head.node_value() <= current_node.node_value():

                list2.head = new_l2_head
                if current_node == self.head:
                    self.head = node_to_add
                    self.head.next = current_node
                else:
                    previous_node.next = node_to_add
                    node_to_add.next = current_node
                    current_node = node_to_add
                continue
            if current_node.next is None:
                current_node.next = node_to_add
                list2.head = None
                # list2.head.next = None
                break

            previous_node = current_node
            current_node = current_node.next

        return print(self)



if __name__ == '__main__':
    ll = LinkedList([1,2,4])
    ll2 = LinkedList([1,3,4])
    # arr = [1,3,4]
    # print(ll.head)
    # print(ll.get_length())
    # ll.add_node(3, 5)
    print(ll)
    print(ll2)
    ll.combine_sorted_lists(ll2)
    pass