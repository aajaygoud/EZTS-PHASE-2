# exp=list(map(str,input().split()))
# stack=[]
# flag=1
# if len(exp)%2!=0:
#     print("Paraenthesis is not matched")
# else:
#     for i in range(len(exp)):
#         if (exp[i]=='('):
#             stack.append(')')
#         elif exp[i]=='[':
#             stack.append(']')
#         elif exp[i]=='{':
#             stack.append('}')
#         elif (exp[i]==')'or exp[i]==']'or exp[i]=='}'):
#             if exp[i]==stack[-1]:
#                 stack.pop()
#             else:
#                 print("Not Balanced")
#                 flag=0
#                 break
#     if flag:
#         print("balanced")

exp=input("Enter expression: ")
stack=[]
flag=0
if len(exp)%2!=0:
    print("Paraenthesis is not matched")
else:
    for i in range(len(exp)):
        if (exp[i]=='(' or exp[i]=='['or exp[i]=='{'):
            stack.append(exp[i])
        elif(exp[i]==')' or exp[i] == ']' or exp[i] == '}'):
            if(stack[-1]=='(' and exp[i]==')' or stack[-1] == '[' and exp[i] == ']'or stack[-1] == '{' and exp[i] == '}' ):
                stack.pop()
                flag=1

    if flag==1:
        print("Balanced")
    else:
        print("Not balanced")




