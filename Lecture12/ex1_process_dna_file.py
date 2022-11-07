
my_file = open("input.txt",'r')
new_file = open("new_file.txt",'w')


for line in my_file:
	print(line)
	dna = line[14:len(line)]
	print("The length post adapter cut is ", len(dna))
	new_file.write(str(dna) + "\n")

my_file.close()
new_file.close()
