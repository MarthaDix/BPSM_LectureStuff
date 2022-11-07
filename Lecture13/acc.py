accessions = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accessions :
	if acc.startswith('b') :
		print(acc + " start with  b")
	elif acc.startswith('a'):
		print(acc + " start with a")
	elif acc.startswith('h') :
		print(acc + " start with h")
	else:
		print(acc + " starts with something else")
