def calculate_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth


birth_year = int(input("What is your year of birth? "))
age = calculate_age(birth_year)

if age > 120:
    print("Hey Old Man!!!")
else:
    print(age)

