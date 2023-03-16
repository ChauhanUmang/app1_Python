contents = []

file = open('../files/Day6/a.txt', 'r')
contents.append(file.read())
file.close()

file = open('../files/Day6/b.txt', 'r')
contents.append(file.read())
file.close()

file = open('../files/Day6/c.txt', 'r')
contents.append(file.read())
file.close()

for i in contents:
    print(i)