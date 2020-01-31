# from dll_stack import Stack
# from dll_queue import Queue
import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check to see if the value is greater than the root
        if value < self.value:
            # see if there's a node left, if not make it
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # check to see if the value is less than the root
        if value > self.value:
            # check if there's a node right, if not make it.
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # if nodes are there already, insert new value
        # check if val is in tree
        elif value == self.value:
            return "Value exists in tree already"

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check value is equal to the target
        if self.value == target:
            return True
        # check right for contains
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
        # check left for contains
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
            # default case
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # pass in cb with value
        cb(self.value)
        # count left side
        if self.left:
            self.left.for_each(cb)
        # count right side
        if self.right:
            self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

