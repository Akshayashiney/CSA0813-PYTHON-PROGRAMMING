import matplotlib.pyplot as plt
products = ["A", "B", "C", "D"]
sales = [40, 60, 80, 100]
plt.bar(products, sales, color=['blue', 'green', 'orange', 'red'])
plt.title("Sales of Different Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
