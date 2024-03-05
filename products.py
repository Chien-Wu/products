#讀取檔案
data = []
with open("products.csv", "r", encoding = "utf-8") as f:
	for line in f:
		if "products name, products price" in line:
			continue
		s = line.strip().split(",")
		data.append(s)
print(data)

#讓使用者輸入
while True:
	name = input("enter product name:")
	if name == "q":
		break
	price = input("enter product price:")
	price = int(price)
	data.append([name, price])
print(data)

#印出所有購買紀錄
for p in data:
	print(p[0], "is", p[1], "dollars")

#寫入檔案
with open("products.csv", "w", encoding = "utf-8") as f:
	f.write("product name, product price\n")
	for p in data:
		f.write(p[0] + "," + str(p[1]) + "\n")
