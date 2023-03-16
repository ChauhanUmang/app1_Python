def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)


user_prompt = input("Enter names separated by commas (no spaces): ")
nu_of_names = get_nr_items(user_prompt)
print(nu_of_names)