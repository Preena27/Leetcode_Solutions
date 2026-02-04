class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            if path:
                path = path + "->" + str(node.val)
            else:
                path = str(node.val)
            
            if not node.left and not node.right:
                res.append(path)
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return res
