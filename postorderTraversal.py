class Solution(object):
    def postorderTraversal(self, root):
        result=[]
        def postorder(root):
            if root is not None:
                postorder(root.left)
                postorder(root.right)
                result.append(root.val)
            
        postorder(root)
        return result
