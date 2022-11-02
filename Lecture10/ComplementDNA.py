DNA="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print(DNA)

DNA=DNA.replace("T","X")
DNA=DNA.replace("A","T")
DNA=DNA.replace("X","A")

DNA=DNA.replace("G","X")
DNA=DNA.replace("C","G")
DNA=DNA.replace("X","C")

print(DNA)
