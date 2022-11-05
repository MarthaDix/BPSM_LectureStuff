#!/usr/bin/python3

with open("plain_genomic_seq.txt") as local_seq_file:
	local_seq = local_seq_file.read()
	bases = ['A', 'C', 'T', 'G']
	local_seq_clean = ''.join([i for i in local_seq if i in bases])
	print(local_seq_clean)
	exon1=local_seq_clean[0:63]
	intron1=local_seq_clean[63:91]
	exon2=local_seq_clean[91:len(local_seq_clean)]

intron1file = open("local_intron1.fasta", "w")
intron1file.write("> local intron 1 " + str(len(intron1)) + " bases\n")
intron1file.write(intron1+"\n")
intron1file.close()

intron1file = open("local_exon1.fasta", "w")
intron1file.write("> local exon 1 " + str(len(exon1)) + " bases\n")
intron1file.write(exon1+"\n")
intron1file.close()

intron1file = open("local_exon2.fasta", "w")
intron1file.write("> local exon 2 " + str(len(exon2)) + " bases\n")
intron1file.write(exon2+"\n")
intron1file.close()


with open("AJ223353.cds.na.fa") as file:
	info = file.read()
	print(type(info))
	range = info.split("location=")[1].split("]")[0]
	start = range.split("..")[0]
	end = range.split("..")[1]
	print(start, " ", end)

with open("AJ223353_nohead.fa") as file:
	seq = file.read()
	intron_1 = seq[0:int(start)]
	extron = seq[int(start):int(end)]
	intron_2 = seq[int(end):len(seq)]


intron1file = open("AJ223353_non_coding1.fasta", "w")
intron1file.write("> remote non cosing  1 " + str(len(intron_1)) + " bases\n")
intron1file.write(intron_1+"\n")
intron1file.close()

intron1file = open("A223353_non_coding_2.fasta", "w")
intron1file.write("> remote non coding 2" + str(len(intron_2)) + " bases\n")
intron1file.write(intron_2+"\n")
intron1file.close()

intron1file = open("AJ223353_coding2.fasta", "w")
intron1file.write("> remote coding  " + str(len(extron)) + " bases\n")
intron1file.write(extron+"\n")
intron1file.close()

