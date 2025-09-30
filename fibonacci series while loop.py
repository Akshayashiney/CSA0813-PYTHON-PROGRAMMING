a=eval(input("enter the range:"))
i=0
first_value=0
second_value=1
while(i<a):
    if(i<=1):
        Next=i
    else:
        Next=first_value+second_value
        first_value=second_value
        second_value=Next
    print(Next)
    i=i+1