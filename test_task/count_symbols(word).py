def count_symbols(word):
	counter = {}
	for letter in word:
		if letter in counter:
			counter[letter] +=1
		else:
			counter[letter] = 1
	return counter


print(count_symbols('100500'))
print(count_symbols(r'\## &&& $$$$ *****'))