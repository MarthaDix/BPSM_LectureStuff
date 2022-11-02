DNA="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif="GAATTC"

print(DNA)

pos=DNA.find(motif,0)

print("First fragement: ", pos+2)
print("Second fragement: ", len(DNA)-(pos+2)) 
