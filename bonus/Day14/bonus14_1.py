from bonus.Day14 import parsers as ps
from bonus.Day14 import converters as cs

feet_inches = input("Enter feet and inches: ")

parsed = ps.parse(feet_inches)
result = cs.convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide.")
