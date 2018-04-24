import node

class BinanryTree:

    def __init__(self):
        self.root =  None

    def addNode(self, data):
        return Node(data)

    def insert(self, root, data):
        if root = None:
            return self.addNode(data)
        else:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def search(self, root, target):
        if root = None:
            return 0
        else:
            if target == root.data
                return 1
            else:
                if target < root.data:
                    return self.search(root.left, target)
                else:
                    return self.search(root.right, target)
