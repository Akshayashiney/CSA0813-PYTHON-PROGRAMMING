print("------ Currency Converter ------")
print("1. INR to USD")
print("2. USD to INR")
choice = int(input("Enter your choice (1 or 2): "))
amount = float(input("Enter amount: "))
if choice == 1:
    result = amount * 0.012
    print(amount, "INR =", result, "USD")
elif choice == 2:
    result = amount * 83
    print(amount, "USD =", result, "INR")
else:
    print("Invalid choice!")