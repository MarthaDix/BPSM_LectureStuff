
genomic = open("genomic_dna2.txt",'r')
genomic_data = genomic.read()
exons = open("exons.txt",'r')
exon_file = open("exon_file.txt", 'w')

exon_str = ""
for exon in exons:
	exon = exon.strip()
	exon_list = exon.split(',')
	dna = genomic_data[int(exon_list[0]):int(exon_list[1])]
	exon_str = exon_str + str(dna)

exon_file.write(exon_str + "\n")

genomic.close()
exons.close()
exon_file.close()
