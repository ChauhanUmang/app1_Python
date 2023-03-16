file = open('../files/Day6/members.txt', 'r')
members_list = file.readlines()
file.close()

new_member = input("Add a new member:")
members_list.append(new_member + '\n')

file = open('../files/Day6/members.txt', 'w')
file.writelines(members_list)
file.close()

