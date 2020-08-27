"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

Note: The merging process must start from the root nodes of both trees.
"""





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if not t1 and not t2:
            return None
        
        def mergeNodes(new, t1, t2):
            """Merging t1 and t2 nodes into new node"""
            
            if t1 and t2:
                new.val = t1.val + t2.val
            elif not t1:
                new.val = t2.val
            elif not t2:
                new.val = t1.val
        
        new = TreeNode()
        
        to_check = [(new, t1, t2)] #store tuples of new node and corresponding t1 and t2 node
        
        while to_check:
            
            curr, curr_t1, curr_t2 = to_check.pop()
            
            mergeNodes(curr, curr_t1, curr_t2)
            
            if  (curr_t1 and curr_t1.left) or (curr_t2 and curr_t2.left):
                curr.left = TreeNode()
                t1_left = curr_t1.left if curr_t1 else None
                t2_left = curr_t2.left if curr_t2 else None
                to_check.append((curr.left, t1_left, t2_left))
            
            if (curr_t1 and curr_t1.right) or (curr_t2 and curr_t2.right):
                curr.right = TreeNode()
                t1_right = curr_t1.right if curr_t1 else None
                t2_right = curr_t2.right if curr_t2 else None
                to_check.append((curr.right, t1_right, t2_right))
                
        return new