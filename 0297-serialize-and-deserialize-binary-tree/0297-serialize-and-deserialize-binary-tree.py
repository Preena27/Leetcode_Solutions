# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    MARKER = "M"
    def serialize_rec(self, node, stream):
        if node is None:
            stream.append(self.MARKER)
            return
        stream.append(str(node.val))
        self.serialize_rec(node.left, stream)
        self.serialize_rec(node.right, stream)

    def serialize(self, root):
        stream = []
        self.serialize_rec(root, stream)
        return ','.join(stream)

    def deserialize_helper(self, values):
        val = values.pop(0)
        if val == self.MARKER:
            return None
        node = TreeNode(int(val))
        node.left = self.deserialize_helper(values)
        node.right = self.deserialize_helper(values)
        return node
    def deserialize(self, data):
        values = data.split(',') 
        return self.deserialize_helper(values)
