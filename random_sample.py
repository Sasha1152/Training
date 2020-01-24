import random

messages = ['It is certain',
            'it is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

length = len(messages)
message = random.randint(0, length - 1)

print(messages[message])

####### equivalent random.uniform(n, m):

def rand(a, b):
    return a + (b - a) * random.random()

print(rand(4, 5))