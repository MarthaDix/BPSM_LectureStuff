seqs = ['ATTGRACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']


for seq in seqs:
	count = seqs.index(seq) +1
	while count < len(seqs):
		total=0
		i=0
		while i < len(seq):
			if(seq[i] == seqs[count][i]):
				total+=1
			i+=1
		print(seq, " vs ", seqs[count], " has ", total, " of the same bases at the same positsions")
		count+=1
