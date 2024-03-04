data = []
while True:
	name = input("enter product name:")
	if name == "q":
		break
	price = input("enter product price:")
	price = int(price)
	data.append([name, price])
print(data)

for p in data:
	print(p[0], "is", p[1], "dollars")

with open("products.csv", "w", encoding = "utf-8") as f:
	f.write("product name, product price\n")
	for p in data:
		f.write(p[0] + "," + str(p[1]) + "\n")
