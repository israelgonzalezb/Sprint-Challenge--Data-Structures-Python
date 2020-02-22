from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if we have room in the buffer
        # then add the new item to the end
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # if there is no room in the buffer
            # remove the oldest item in the buffer (head)
            # and add the new item to the buffer
        else:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
