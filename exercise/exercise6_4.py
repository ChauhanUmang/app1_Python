filenames = ['doc1.txt', 'essay1.txt', 'members1.txt']

for filename in filenames:
    file = open(f"../files/Day6/{filename}", 'w')
    file.write("Hello")
    file.close()
