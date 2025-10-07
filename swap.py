a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("\Before swap:a=",a,",b=",b)
temp=a
a=b
b=temp
print("After Swap(with temp):a=",a,",b=",b)
a,b=b,a
print("After Swap(without temp):a=",a,",b=",b)