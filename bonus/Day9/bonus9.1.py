# length of password  > 8
# password contains at least one digit
# password contains at least one upper case letter

def has_numbers(user_password):
    return any(char.isdigit() for char in user_password)


def has_uppercase(user_password):
    return any(char.isupper() for char in user_password)


password = input("Enter a password:")

if len(password) > 8 and has_numbers(password) and has_uppercase(password):
    print("Strong Password")
else:
    print("Weak Password")
