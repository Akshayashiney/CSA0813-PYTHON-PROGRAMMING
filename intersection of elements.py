list1=list(map(int,input("enter first list:").split()))
list2=list(map(int,input("enter second list:").split()))
intersection=list(set(list1)&set(list2))
print("intersection:",intersection)
