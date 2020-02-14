import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# This solution is O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

### New solution ###
# runtime: 0.0747992992401123 seconds
# This solution is O(n log n) b/c you have to loop through both names lists 1 time.
# create a BST
bst = BinarySearchTree(names_1[0])
for i in range(1, len(names_1)):
    bst.insert(names_1[i])

# check if search tree contains duplicates
# loop through list 2
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# for name in names_2:
#     # if name is in names_set append it to dups
#     if name in names_set:
#         duplicates.append(name)
