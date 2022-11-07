import os

path="/localdisk/home/s2341491/Exercises/Lecture12"
files = [f for f in os.listdir(path) if f.endswith('.dna')]
print(files)

#mydir = 100
#while mydir < 1000:
	#os.mkdir(str(mydir))
	#mydir+=100

for file in files:
	with open(file) as myfile:
		seqs = myfile.readlines()
		for seq in seqs:
			print(len(seq))
			output = open(str(len(seq))[0:1]+"00/"+str(len(seq))+file,"w")
			output.write(seq)
			output.close()
