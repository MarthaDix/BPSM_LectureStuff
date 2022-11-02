DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

first_ex = DNA[0:63]
intron = DNA[63:91]
second_ex = DNA[91:len(DNA)]

print(first_ex)
print(intron)
print(second_ex)

coding = first_ex+second_ex
percoding = (len(coding)/len(DNA))*100
print(percoding)

print(first_ex +  intron.lower() +  second_ex)
