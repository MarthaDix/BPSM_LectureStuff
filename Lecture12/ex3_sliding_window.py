size = 30
offset = 6

myfile = open("AJ223353_coding2.fasta","r")
seq = myfile.readlines()[1:]
myfile.close()
seq = "".join([x[:-1] for x in seq])

start = 0
all_data=open("all_data.fasta","w")
#while start <= len(seq)+size and len(seq)-start >= size:
while start <= len(seq)+size and len(seq)-start >= offset:
	myseq = seq[start:start+size]
	gc =  round((myseq.count("G")+myseq.count("C"))/len(myseq),2)
	print("% GC ", gc, " for ", myseq, " len ", len(myseq))
	output = open(str(start)+".fasta", "w")
	output.write(" > seq starting at "+ str(start) + " with GC% "+ str(gc)+"\n")
	output.write(myseq+"\n")
	output.close()

	#all_data = open("all_data.fasta", "w")
	all_data.write(" > seq starting at "+ str(start) + " with GC% "+ str(gc)+"\n")
	
	all_data.write(myseq+"\n")
	#all_data.close()

	start+=offset
all_data.close()
