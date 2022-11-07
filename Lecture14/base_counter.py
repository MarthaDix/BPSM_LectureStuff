
def count_undetermined(seq):
	seq = seq.upper()
	count = 0
	for base in seq:
		if base != "A" and base != "T" and base != "G" and base != "C":
			count+=1
	if count/len(seq) > 0.7:
		return True
	else:
		return False

print(count_undetermined("MMMMMGYYYG"))
