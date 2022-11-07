
def get_percent_aa(seq, aa=["A","I","L","M","F","W","Y","V"]):
	count=0
	for amino in aa:
		for seq_aa in seq:
			if seq_aa == amino:
				count+=1
	return round(count/len(seq),2)

assert round(get_percent_aa("MSRSLLLRFLLFLLLPPLP",["M"])) ==round(1/20)
print(get_percent_aa("MAILFP"))
