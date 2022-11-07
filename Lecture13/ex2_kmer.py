size = 2
offset = 1
n = 3

seq="AAAAAAAATGTCATTTTTTTTTTGTGTGTG"
kmer_dict = {}

start = 0
while start <= len(seq)+size and len(seq)-start >= offset:
	myseq = seq[start:start+size]
	gc =  round((myseq.count("G")+myseq.count("C"))/len(myseq),2)
	if myseq in kmer_dict:
		kmer_dict[myseq]=kmer_dict[myseq]+1	
	else:
		kmer_dict[myseq]=1
	start+=offset
for kmer, count in kmer_dict.items():
	if count >= n:
		print(kmer, " occurs ", count, " times in the sequence")
