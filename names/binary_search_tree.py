class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the root value to the new value being added
        if self.value >= value:
            # if the value is less than the root, move left
            # if no child on that side insert
            if self.left is None:
                self.left = BinarySearchTree(value)
            # else keeping moving left and call insert again
            else:
                self.left.insert(value)
        # if the value is greater than the root, move right
        elif self.value < value:
            # if the value is greater than the root, move right
            # if no child on that side insert
            if self.right is None:
                self.right = BinarySearchTree(value)
            # else keeping moving left and call insert again
            else:
                self.right.insert(value)

    def contains(self, target):
        # look at the root and compare it to  target
        # if the target is less than the current node value,
        if target < self.value:
            # and can move left and repeat
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        # if the target is greater than the current node value move right and repeat
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        # if the target equals the value return true
        elif target == self.value:
            return True
        # if left and right are None return false
        else:
            return False
