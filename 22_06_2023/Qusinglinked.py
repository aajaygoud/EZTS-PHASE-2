class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class q:
    def __init__(self):
        self.head=None
    def enq(self):
        n=int(input("Enter element to enqueue: "))
        if self.head==None:
            self.head=n
            n.next=self.head
            temp=n
        else:
            print("Element to be inserted:")
import queue
a=queue.Queue()
b=queue.Queue()
for i in range(5):
    b.put(x)

