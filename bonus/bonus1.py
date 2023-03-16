temperatures = [10, 12, 14]
file = open('../files/Day7/bug1.txt', 'w')

temperatures = [str(temp) + '\n' for temp in temperatures]

file.writelines(temperatures)