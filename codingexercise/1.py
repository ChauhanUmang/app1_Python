while True:
    with open('../files/Day8/entry.txt', 'r') as file:
        entry_list = file.readlines()

    user_input = input("Throw the coin and enter head or tail here: ?").lower() + '\n'
    entry_list.append(user_input)

    with open('../files/Day8/entry.txt', 'w') as file:
        file.writelines(entry_list)

    num_of_heads = entry_list.count('head\n')
    heads_percentage = num_of_heads / len(entry_list) * 100
    print(f"Heads:{heads_percentage}%")


