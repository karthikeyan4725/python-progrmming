def common_data(list1, list2):
	result = False
	for x in list1:
		for y in list2:
			if x == y:
				result = True
				return result
				
	return result
a = set(input("enter a set 1:"))
b = set(input("enter a set 2:"))
print(common_data(a, b))
