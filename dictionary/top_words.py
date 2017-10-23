import string

text = "Hello! I'm from Lviv, and I like to swim. Hello again!"
text_lowered = text.lower()

black_list = [c for c in string.punctuation if c != "'"]

for symbol in black_list:
    text_lowered = text_lowered.replace(symbol, '')

print(text_lowered)
    
cleaned_words = text_lowered.split()
unique_words = set(cleaned_words)

word_count = {}

for word in unique_words:
    word_count[word] = cleaned_words.count(word)
    
print(word_count)


top_words = {}


for word, count in word_count.items():
    if count in top_words:
        top_words[count].append(word)
    else:
        top_words[count] = [word]
        
print(top_words)
