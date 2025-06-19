# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []
        ended = False
        answer = []
        track_list = [] # 0 for right, 1 for left
        string = str(root.val) + "->"
        while 1:
            if ended:
                if root.right and track_list[-1] == 1:
                string += str(root.right.val)  + "->"
                root = root.right
                track_list = track_list[:-1]
                track_list.append(0)
            elif root.left and track_list[-1] == 1:
                string += str(root.left.val) + "->"
                root = root.left
                track_list = track_list[:-1]
                track_list.append(1)
            else:
                answer.append(string[:-2])
                root = root.parent
                ended = True
            else:
                if root.right:
                    string += str(root.right.val)  + "->"
                    root = root.right
                    track_list.append(0)
                elif root.left:
                    string += str(root.left.val) + "->"
                    root = root.left
                    track_list.append(1)
                else:
                    answer.append(string[:-2])
                    root = root.parent
                    ended = True
# print(Solution().binaryTreePaths( root = [1,2,3,None,5]))
k = [1, 2, 3, 4, 5]
print(k[:-1])