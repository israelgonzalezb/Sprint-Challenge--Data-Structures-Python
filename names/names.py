import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Going to try to use BST for this
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return
        if self.value is None: # check to see if tree has a root
            self.value = BinarySearchTree(value) # if there's no root, make this new value the root
        elif value >= self.value: # passed in value is greater than current node, so move right
            # ...
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else: # otherwise, go left
            # ...
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
            
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base cases:
        # target found or we hit None
        if self.value == target:
            # print(f"Value of the node and target are the same, value is {self.value}, target is {target}, are they equal? {self.value == target}")
            return True
        # Recursive case
        # go down left or right subtree, depending on target
        elif self.value:
            # print(f"Value and target are not the same. self.value is {self.value}, target is {target}")
            if target > self.value and self.right:
                return self.right.contains(target)
            elif target < self.value and self.left:
                return self.left.contains(target)
            else:
                return False

# -------------------


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
bst = BinarySearchTree(names_1[0])

for name_1 in names_1[1:]:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#             names_2.remove(name_2)
#             break

            
"""
# start a parallel linear search from both ends of each list
for i in range(len(names_1)):
    for name_2 in names_2.sort():
        if names_1[i] == name_2 or names_1[len(names_1)-i-1] == name_2:
            duplicates.append(name_2)
            names_2.remove(name_2)
            break
# once a match is found, add it to the duplicates list
# remove the found duplicate from both names lists
"""

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
