    def preorderTraversal(self, root):
        result=[]
        def preorder(root):
            if root is not None:
                
                result.append(root.val)
                preorder(root.left)
                preorder(root.right)
            
        preorder(root)
        return result
