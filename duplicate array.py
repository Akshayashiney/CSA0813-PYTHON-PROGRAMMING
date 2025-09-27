arr=list(map(int,input("enter elements:").split()))
duplicates=list(set([x for x in arr if arr.count(x)>1]))
print("duplicate elements:",duplicates)