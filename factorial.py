a=[]
fact=[]
ch="y"
while ch=="y" or ch=="Y":
    item=int(input("Enter the element of list:"))
    a.append(item)
    ch=input("do you want to enter more element:")
print("the list is:",a)
for i in a:
    f=1
    for j in range(1,i+1):
        f=f*j
    fact.append(f)
print("the factorial of each element is:",fact)