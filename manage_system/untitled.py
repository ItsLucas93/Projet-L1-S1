path = "../data/readers.txt"

with open(path, "r") as f:
	data = f.readlines()

	for i in range(0, len(data)):
		data[i] = data[i].split(",")
	print(data)
