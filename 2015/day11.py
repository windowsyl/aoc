alphabet = 'abcdefghjkmnpqrstuvwxyz'
password = list('abcdefgh')

def increment(word):
    if word[-1] == 'z': return increment(word[:-1]).append('a')
    else:
        word[-1] = alphabet[alphabet.index(password[-1])+1]
        return word

while True:
    word = increment(word)
    

print(''.join(password))