
def get_percent_aa(seq, aa):
	return round(seq.count(aa)/len(seq),2)

assert round(get_percent_aa("MSRSLLLRFLLFLLLPPLP","M")) ==round(1/20)
