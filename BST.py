class TreeNode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None

def arr_to_bst(nums):
    if not nums:
        return None
    
    mid = len(nums)//2
    root= TreeNode(nums[mid])

    root.left=arr_to_bst(nums[:mid])
    root.right= arr_to_bst(nums[mid+1:])
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

if __name__=="__main__":
    nums=[1,2,3,4,5,6,7]
    root=arr_to_bst(nums)
    print("inorder traversal of BST: ")
    inorder(root)