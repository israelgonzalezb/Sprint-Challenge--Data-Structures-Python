from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.ring_index = 0

    def append(self, item):
       
        # if there is nothing in the buffer
        # make the first appended item the head, to init the DLL
        # make this item the "current" node of concern
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
            self.ring_index = 1
            return
        
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.ring_index += 1
            
        elif self.ring_index < self.capacity:
            self.current.next.delete()
            self.current.insert_after(item)
            self.current = self.current.next
            self.ring_index += 1


        elif self.ring_index == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
            self.ring_index = 1
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Check if we have anything in the buffer
        # If there is no head in the DLL, then that means there is nothing in the buffer
        # so skip the condition block and return the empty list
        if self.storage.head:
            # if there is an item at the head
            # append the value to the list_buffer_contents list
            list_buffer_contents.append(self.storage.head.value)

            # do the same for the subsequent next values, checking up to the dll's length minus one
            current_item = self.storage.head
            for i in range(self.storage.length-1):
                list_buffer_contents.append(current_item.next.value)
                current_item = current_item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
