import os

#讀取檔案
def read_file(filename):
	data = []
	if os.path.isfile(filename):
		with open(filename, "r", encoding = "utf-8") as f:
			for line in f:
				if "product name, product price" in line:
					continue
				s = line.strip().split(",")
				data.append(s)
			print(data)
			return data

#讓使用者輸入
def input_products(data):
	while True:
		name = input("enter product name:")
		if name == "q":
			break
		price = input("enter product price:")
		price = int(price)
		data.append([name, price])
	print(data)
	return data

#印出所有購買紀錄
def print_products(data):
	for p in data:
		print(p[0], "is", p[1], "dollars")

#寫入檔案
def write_file(filename, data):
	with open(filename, "w", encoding = "utf-8") as f:
		f.write("product name, product price\n")
		for p in data:
			f.write(p[0] + "," + str(p[1]) + "\n")

data = read_file("products.csv")
data = input_products(data)
print_products(data)
write_file("products.csv", data)



