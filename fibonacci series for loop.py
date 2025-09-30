number=int(input("enter the range:"))
first_value=0
second_value=1
for num in range(0,number):
    if(num<=1):
        Next=num
    else:
        Next=first_value+second_value
        first_value=second_value
        second_value=Next
    print(Next)