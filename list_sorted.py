some_list = [5, 6, 0, -4, 55, 444, 48, 1]

sorted_list = []
while some_list:
	sorted_list.append(min(some_list))
	some_list.remove(min(some_list))

print sorted_list