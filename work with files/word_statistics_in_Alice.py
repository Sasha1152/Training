def word_statistics(my_file, word2):

    def get_key(value):
        for k, v in dictionary.items():
            if v == value:
                return k

    text = open(my_file, 'r')
    dictionary = {}
    top_twenty_freq = []
    top_twenty_word = []
    
    a = text.read()
    a = a.lower()
    a = a.split()
    longest_word = ''
    for word in a:
        if len(word) > len(longest_word):
            longest_word = word
    print('longest word in text is "' + str(longest_word) + '"')
    print('the word "' + str(word2) + '" inserts in text ' + str(a.count(word2)) + ' times')

    for element in a:
        if element in dictionary.keys():
            dictionary[element] += 1
        else:
            dictionary[element] = 1

    while len(top_twenty_freq) < 20:
        top_twenty_freq.append(max(dictionary.values()))
        top_twenty_word.append(get_key(max(dictionary.values())))
        del dictionary[get_key(max(dictionary.values()))]
    for i in range(20):
        print(str(top_twenty_freq[i]) + ': ' + str(top_twenty_word[i]))

    text.close()

word_statistics('alice_in_wonderland.txt', 'alice')
