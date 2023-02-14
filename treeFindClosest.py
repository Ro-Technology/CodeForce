class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def data_insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.data_insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.data_insert(data)
   
        else:
            self.data = data
            
    def searchVal(self, data):
        if data < self.data:
            if self.left is None:
                return str(data)+" is not Found in the Binary Tree"

            return self.left.searchVal(data)
        elif data > self.data:
            if self.right is None:
                return str(data)+" is not Found in the Binary Tree"
            return self.right.searchVal(data)
        else:
            return str(self.data) + " is found in the Binary Tree"