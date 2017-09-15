testing_list = [1, 2, 3, 4, 0, -1, 4, 5, 6, 7, 8, 9]

print(testing_list[0])
print(testing_list[1])
# 1. Find minimal element of list using `for` loop.
number_min = testing_list[0]
for number in testing_list:
    if number < number_min:
        number_min = number
print(number_min)
       
# 2. Find minimal element of list using `while` loop.
index = 0
while index != len(testing_list) - 1:
    if testing_list[index] < number_min:
        number_min = testing_list[index]
    index += 1
print(number_min)

# 3. Find minimal element of list using `built-in` function.
print(min(testing_list))

# 4. Replace third element (`world`) with sorted string of these letters.
testing_tuple = (2, 3, 'world', [1, 2, 3], 8)

#testing_list = []
#for element in testing_tuple:
    #testing_list.append(element)
testing_list2 = [element for element in testing_tuple]    
new_list = sorted(list(testing_list2[2]))
string = ''
for letter in new_list:
    string += str(letter)

testing_list2[2] = string
testing_tuple = tuple(testing_list2)
print(testing_tuple)
print('-' * 50)

# 5. Catch possible errors for previous tasks.
i = 1
modern_list = []
for element in testing_list:
    if i == len(testing_list):
        break
    try:
        new_element = float(testing_list[i - 1]) / float(testing_list[i])
        modern_list.append(new_element)
        print(str(testing_list[i - 1]) + ' / ' + str(testing_list[i]) + ' = ' + str(new_element))
    except ZeroDivisionError:
        print('Throw away zero from the list')   
    finally:
        print('*  ' * 10)
        i += 1
print(modern_list)