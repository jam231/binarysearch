import Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Solution for [Medium] Sibling Tree Value problem from binarysearch.com
    Problem is finding in input Binary Search Tree value of sibling node to the node that contains value k.
    Solution is guaranteed to exists (ergo, root node cannot contain value k) and every node in BST either has both children
    or none.

    Time complexity: O(h) where h is tree height
    Space complexity: O(h) for recursive stack, where h is tree height. It could be improved to O(1) by iterative tree traversal
    storing only current node.
    """
    def solve(self, root, k):
        assert root.val != k
        assert (root.left and root.right) or (not root.left and not root.right)

        if root.left.val == k:
            return root.right.val
        elif root.right.val == k:
            return root.left.val
        
        if root.val < k:
            return self.solve(root.right, k)
        else:
            return self.solve(root.left, k)
