# without flag
def linear_search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i+1 # function ends on encountering this line
	
	return -1 # sentinel value

arr = [10, 9, 12, 7, 6, 2]
print(arr)
x = int(input("Enter the element for linear search: "))

pos = linear_search(arr, x)
if pos == -1:
	print("Result: Element not found")
else:
	print("Result:", pos)