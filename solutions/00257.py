"""
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/description/
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(V+E)   # Vertex + Edge
    Space:  O(V)     # Vertex

    DFS
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.val is None:
            return []

        def traverse(node):
            if node.left is None and node.right is None:
                return [[node.val]]
            
            paths = []
            if node.left is not None:
                for path in traverse(node.left):
                    paths.append([node.val]+path)
            if node.right is not None:
                for path in traverse(node.right):
                    paths.append([node.val]+path)
            return paths

        paths = traverse(root)
        paths = ["->".join([str(i) for i in path]) for path in paths]
        return paths


class Solution:
    """
    Time:   O(V+E)   # Vertex + Edge
    Space:  O(V)     # Vertex

    DFS
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.val is None:
            return []

        def traverse(node):
            if node.left is None and node.right is None:
                return [str(node.val)]
            
            paths = []
            if node.left is not None:
                for path in traverse(node.left):
                    paths.append(str(node.val)+"->"+path)
            if node.right is not None:
                for path in traverse(node.right):
                    paths.append(str(node.val)+"->"+path)
            return paths

        paths = traverse(root)
        return paths


class Solution:
    """
    Time:   O(V+E)   # Vertex + Edge
    Space:  O(V)     # Vertex

    DFS
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        queue = [[root,""]]
        result = []
        while len(queue)!=0:
            node,path = queue.pop()
            if not node.left and not node.right:
                result.append(path+str(node.val))
            if node.left:
                queue.append([node.left,  path+str(node.val)+"->"])
            if node.right:
                queue.append([node.right, path+str(node.val)+"->"])
        return result
