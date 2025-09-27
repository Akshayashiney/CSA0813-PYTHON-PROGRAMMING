import statistics
data=list(map(int,input("enter numbers:").split()))
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
average=(mean+median+mode)/3
print("mean:",mean)
print("mode:",mode)
print("median:",median)
print("average of mean,median,mode:",average)