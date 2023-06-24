class Node:
    def __init__(self,data):
        #data=int(input("Enter node to insert: "))
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self):
        n=int(input("Enter element to be pushed: "))
        if self.head==None:
            self.head=n
            n.next=None
        else:
            temp=self.head
            n.next=temp
            self.head=n
    def pop(self):
        if self.head==None:
            print("Stack is empty")
        else:
            self.head=self.head.next
            print("Element removed succesfully: ",self.head.data)
    def display(self):
        if self.head==None:
            print("Stack is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next
a=Node(10)
n=Node(20)
b=Stack()
while True:
    num=int(input("\nEnter the operation: \n1.push\n2.pop\n3.display\n4.exit\n"))
    if num==1:
        b.push()
    elif num==2:
        b.pop()
    elif num==3:
        b.display()
    else:
        print("Invalid")




