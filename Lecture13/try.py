y = 12
x = 3

try:
	if x > y:
		print(x, " is bigger than ", y)
except NameError:
	print("One of the variables wasnt defined it seems ..")
except:
	print("Someing not right!")
finally:
	print("Done using the try:Except test")
