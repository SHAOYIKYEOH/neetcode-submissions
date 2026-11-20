# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

    # height = 1 + max(left h, right h)
    # diameter = left height + right height

        self.res = 0

        # create a nested function to return the height
        def height(curr):
            if not curr:
                return 0

            left = height(curr.left)
            right = height(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        height(root)
        return self.res    



        