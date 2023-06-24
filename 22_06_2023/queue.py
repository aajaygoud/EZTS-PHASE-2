a=[]
def enqueue():
    n=int(input("Enter element to push into queue: "))
    a.append(n)
    print("Element pushed successfully: ",end=" ")
    print(a)


def dequeue():
    if a==[]:
        print("List is empty")
    else:
        print("Element poped sucessfully: ",a.pop(0))

def display():
    if a==[]:
        print("List is empty")
    else:
        print(a)

while True:
    num=int(input("\nEnter the operation: \n1.enqueue\n2.dequeue\n3.display\n4.exit\n"))
    if num==1:
        enqueue()
    elif num==2:
        dequeue()
    elif num==3:
        display()
    else:
        break
