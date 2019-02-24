text = 'When I was One I had just begun When I was Two I was nearly new'
words = ['i', 'was', 'three', 'near', 'a']


def words_counter(text: str, words: list) -> dict:
	text = text.lower()
	counter = {word: 0 for word in words}
	text_list = text.split()
	for word in words:
		counter[word] = text_list.count(word)
	return counter

print(words_counter(text, words))
