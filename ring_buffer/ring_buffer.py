from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if length of storage is zero
        if len(self.storage) == 0:
            # if is set new item to head
            self.storage.add_to_head(item)
            # and set current to head
            self.current = self.storage.head
        # elif length of strorage list is less than capacity
        elif len(self.storage) < self.capacity:
            # add new item to the tail of list
            self.storage.add_to_tail(item)
        # elif storage list is at capacity
        elif len(self.storage) == self.capacity:
            # Check if self.current.next is None
            if self.current.next:
                # replace value of current with new item
                self.current.value = item
                # increment the current item to next node
                self.current = self.current.next
            else:
                 # replace value of current with new item
                self.current.value = item
                # increment the current item back to beginning of list
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # start at beginning of list
        node = self.storage.head
        while(node):
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents


ring = RingBuffer(4)
ring.append("a")
ring.append("b")
ring.append("c")
ring.append("d")
ring.append("e")
ring.append("f")
ring.append("g")
ring.append("h")
ring.append("i")
# ring.append("j")
# ring.append("k")
print(ring.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
