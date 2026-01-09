# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        rl = []
        queue = []
        queue.append(root)
        if not root:
            return []
        while queue:
            temp = []
            level_size = len(queue)
            for i in range(level_size):
                popped = queue[0]
                temp.append(queue[0].val)
                del queue[0]
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            rl.append(temp)

        return rl
            
            
        