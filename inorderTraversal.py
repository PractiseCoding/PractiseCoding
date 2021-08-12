class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        def inorder(root):
            if root is not None:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
            
        inorder(root)
        return result
