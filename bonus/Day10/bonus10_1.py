try:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    if length == width:
        exit("That looks like a square.")

    print(length * width)
except ValueError:
    print("Please enter a number.")