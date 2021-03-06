class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        # have a prev var containing the previous pointer
        prev = None
        # start at beginning of LL
        current = self.head
        while(current):
            # store self.head.next_node as next move
            next_move = current.next_node
            # set the next node the prev value
            current.next_node = prev
            # increment prev
            prev = current
            # increment to next node in list
            current = next_move
        self.head = prev


llist = LinkedList()
llist.add_to_head(1)
llist.add_to_head(2)
llist.add_to_head(3)
llist.add_to_head(4)
llist.add_to_head(5)
print(llist.head.get_value())
llist.reverse_list()
print(llist.head.get_value())
