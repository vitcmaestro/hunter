class bstnode():
    def _init_(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    def insert(self,node):
        if(self.key > node.key):
            if(self.left is None):
                self.left = node
                node.parent = self
            else:
                self.left.insert(key)
        else:
            if(self.right is None):
                self.right = node
                node.parent = self
            else:
                self.right.insert(key)
    def inorder():
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
class bsttree(bstnode):
    def _init_(self):
        self.root = None
    def add(self,key):
        newnode = bstnode(key)
        if self.root is not None:
            self.root.insert(key)
        else:
            self.root = newnode
    def inorder(self):
        if(self.root is not None):
            self.root.inorder()
        
 
n =int(input())
a = list(map(int,input().split()))
bst = bsttree()
for i in a:
    bst.add(i)
bst.inorder(self)


