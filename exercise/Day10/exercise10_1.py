try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percent = (value/total_value) * 100
    print(f"That is {percent}%")
except ValueError:
    print("You need to enter a number. Run the program again.")