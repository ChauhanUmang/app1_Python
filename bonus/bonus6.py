contents = ["All carrots are to be sliced longitudinally.", "The carrots were reportedly sliced.", "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for i in range(len(contents)):
    filepath = filenames[i]
    file = open(f"../files/{filepath}", 'w')
    file.write(contents[i])
    file.close()


