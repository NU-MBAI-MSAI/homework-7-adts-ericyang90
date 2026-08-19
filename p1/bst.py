class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is None or not isinstance(other, Node):
            return False
        else:
            return self.val == other.val and self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(self.val)

class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, number):
        # This is a nested function - it's only needed inside this function.
        def insert_node(tree):
            if number < tree.val and tree.left is not None:
                insert_node(tree.left)
            elif number < tree.val:
                tree.left = Node(number)
            elif number > tree.val and tree.right is not None:
                insert_node(tree.right)
            elif number > tree.val:
                tree.right = Node(number)
        if self.root is None:
            self.root = Node(number)
        else:
            insert_node(self.root)

    def __eq__(self, other):
        return self.root == other.root

    @staticmethod
    def create(nodes):
    #creates a BST using the list that is passed in.
    #the first element of the list is set as the root of the BST
    #the remainder of the nodes of the BST are created from the list using the insert_node method
        tree = BST()
        if nodes:
            tree.root = Node(nodes.pop(0))
            for node in nodes:
                tree.insert(node)
        return tree

    def traverse_pre(self):
        traverse_vals = []
        traverse_nodes = []
        #tree.root, tree.left, tree.right are Node objects

        #add root to list
        #set current node as the root
        traverse_nodes.append(self.root)
        traverse_vals.append(self.root.val)
        curr_node = self.root

        keep_loop = True

        #start recursing
        while keep_loop:
            #check if curr_node has a left node that is not in the list traverse already
            #if yes, then add the value of that node to the list, and set curr_node to the left node
            if curr_node.left is not None and curr_node.left not in traverse_nodes:
                traverse_nodes.append(curr_node.left)
                traverse_vals.append(curr_node.left.val)
                curr_node = curr_node.left

            #if no, then check if curr_node has a right node that is not in the list traverse already
            #if yes, then add the value of that node to the list, and set curr_node to the right node
            elif curr_node.right is not None and curr_node.right not in traverse_nodes:
                traverse_nodes.append(curr_node.right)
                traverse_vals.append(curr_node.right.val)
                curr_node = curr_node.right

            elif curr_node == self.root:
                keep_loop = False

            #if there is neither a left node or a right node that is not part of the list
            #  set the curr_node as the parent of the current node
            #  to determine the parent, find the index of the current node in the list traverse_nodes
            #       then, set curr_node as the index before that
            else:
                curr_node = traverse_nodes[traverse_nodes.index(curr_node)-1]

        return traverse_vals

if __name__ == '__main__':
    nodes = [25, 20, 30, 29, 35, 15, 22]
    tree = BST.create(nodes)
    print(tree.traverse_pre()) # -> This should return the list [25, 20, 15, 22, 30, 29, 35]
    # print(tree.traverse_post()) # -> This should return the list [15, 22, 20, 29, 35, 30, 25]