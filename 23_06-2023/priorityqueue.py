st=[]
st.append((1,"ajay"))
st.append((2,"Nataraj"))
st.append((3,"praneeth"))
st.append((4,"Nithin"))
st.sort(reverse=True)
print("The sorted array is: \n")
print(st)

print("The original list is:")
while st:
    print(st.pop(),end=" ")

