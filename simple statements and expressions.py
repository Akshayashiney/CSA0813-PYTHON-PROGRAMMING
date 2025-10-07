import math
a=input("Enter first number:")
b=int(input("Enter second number:"))
a,b=b,a
print("After exchange:a=",a,"b=",b)
print("\n-------------------------------------------\n")
n=int(input("How namy values?"))
values=[]
for i in range(n):
    values.append(input("Enter value{i+1):"))
values=[values[-1]]+values[:-1]
print("After circulation:",values)
print("\n------------------------------------------\n")
x1=float(input("Enter x1:"))
x2=float(input("Enter x2:"))
y1=float(input("Enter y1:"))
y2=float(input("Enter y2:"))
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance:",distance)