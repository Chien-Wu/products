data = []

while True:
	name = input("enter product name:")
	if name == "q":
		break
	price = input("enter product price:") 
	data.append([name, price])

print(data)
