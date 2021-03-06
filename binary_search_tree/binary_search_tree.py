import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #First Compare with root 
        if value < self.value:
            #if value is less then be a left child
            if  self.left is None:
                self.left = BinarySearchTree(value)
                #recurse
            else:
                self.left.insert(value)
            
        else: #when value is greater than root node
            #greater or equal to go right
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
            #if the target is same as the root or for recurse
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        #Check right because the right child is always bigger than its root 
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #Use queue to store the node (fifo)
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            #neighbors of the node will be visited in the order they were inserted
            n = queue.dequeue()
            print(n.value)
            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #Use stack (LIFO) for storage 
        stack = Stack()
        # Push method to add to the stack
        stack.push(node)
        while stack.size > 0:
            n = stack.pop()
            print(n.value)
            #Stack Adjacent nodes
            if n.left:
                stack.push(n.left)
            if n.right:
                stack.push(n.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
