q1,q2,q3,q4,q5 = [],[],[],[],[]

data = open("data.csv")
for line in data:
	sp = line.split(',')
	if (sp[0] == "Drosophila melanogaster" or sp[0] == "Drosophila simulans"):
		q1.append(sp[2])
	if (len(sp[1]) >= 90 and len(sp[1]) <= 110):
		q2.append(sp[2])
	if (((sp[1].upper().count("A")+sp[1].upper().count("T"))/len(sp[1])) < 0.5 and int(sp[3]) > 200):
		q3.append(sp[2])
	if ((sp[2].startswith("k") or sp[2].startswith("h")) and sp[0] != "Drosphila melanogaster"):
		q4.append(sp[2])
	if (((sp[1].upper().count("A")+sp[1].upper().count("T"))/len(sp[1])) > 0.65):
		q5.append(str(sp[2])+" high")
	elif (((sp[1].upper().count("A")+sp[1].upper().count("T"))/len(sp[1])) < 0.45):
		q5.append(str(sp[2])+" low")
	else:
		q5.append(str(sp[2])+" medium")


print("Gene names for species Q1")
print(q1)
print("Gene names for bases Q2")
print(q2)
print("Gene names for AT < 0.5 and expression > 200 Q3")
print(q3)
print("Gene names for begin with k or h Q4")
print(q4)
print("Gene names with rating for Q5")
print(q5)
