n=int(input("enter number of items:"))
total=0.0
for i in range(n):
    price=float(input("Enter price of items:"))
    qty=int(input("enter quantity:"))
    total+=price*qty
print("Total Bill=",total)