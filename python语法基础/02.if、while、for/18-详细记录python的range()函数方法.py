for i in range(5):
	print("i的值是: %d"%(i))


array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array)-1, 0, -1):
	print(i)
	for j in range(0, i):
		print(j, end="")
		if array[j] > array[j+1]:
			array[j], array[j+1] = array[j+1], array[j]
	print("")
print(array)