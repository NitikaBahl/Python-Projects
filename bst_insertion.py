class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Function to insert values in the BST
def bst_insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.val:
        root.left = bst_insert(root.left, value)
    elif value > root.val:
        root.right = bst_insert(root.right, value)  # Corrected here
    return root

# In-order traversal to print the tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    nums = [2, 4, 6, 7, 9]
    root = None
    for num in nums:
        root = bst_insert(root, num)  # Corrected here to insert individual values
    
    print("In-order Traversal of BST after creation:")
    inorder(root)
    print()

    root = bst_insert(root, 8)
    print("In-order Traversal after inserting 8:")
    inorder(root)
    print()