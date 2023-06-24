class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.key==key:
            return root
        elif root.key<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
def search(root):
    search=int(input("\nEnter element to be searched: "))
    flag=0
    while root:
        if root.key==search:
            print("element found")
            flag=1
            break
        elif search<root.key:
            root=root.left
        else:
            root=root.right
    if flag==0:
        print("\nElement not found")

r=Node(100)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,80)
inorder(r)
r=search(r)
