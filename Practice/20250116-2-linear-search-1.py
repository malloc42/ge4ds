# with flag (local)
def linear_search(arr, x):
	flag = 1
	index = 0
	
	for i in range(len(arr)):
		if arr[i] == x:
			flag = 1
			index = i
			break
		else:
			flag = 0 # this block can be removed if flag was declared 0
	
	if flag == 0:
		return "Element not found"
	else:
		return index+1


arr = [10, 9, 12, 7, 6, 2]
print(arr)
x = int(input("Enter the element for linear search: "))

pos = linear_search(arr, x)
print("Result:", pos)