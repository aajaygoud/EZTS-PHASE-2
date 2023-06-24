a=[]
def push():
    n=int(input("Enter element to push into stack: "))
    a.append(n)
    print("Element pushed successfully: ",end=" ")
    print(a)


def pop():
    if a==[]:
        print("List is empty")
    else:
        print("Element poped sucessfully: ",a.pop())

# def display():
#     if a==[]:
#         print("List is empty")
#     else:
#         print(a)
def display():
    exp=int(input("Display 1 for even numbers 0 for odd numbers: \n"))
    if exp==1:
        if a==[]:
            print("stack is empty")
        else:
            c = [ i for i in range(len(a)) if i % 2 == 0]
            print(c)
    elif exp==0:
        if a==[]:
            print("stack is empty")
        else:
            c = [i for i in range(len(a)) if i % 2 != 0]
            print(c)

def peek():
    if a == []:
        print("Stack is empty")
    else:
        print(a[-1])

while True:
    num=int(input("\nEnter the operation: \n1.push\n2.pop\n3.display\n4.peek\n5.exit\n"))
    if num==1:
        push()
    elif num==2:
        pop()
    elif num==3:
        display()
    elif num==4:
        peek()
    else:
        break
c=[ i for i in range(10) if i%2==0]
print(c)