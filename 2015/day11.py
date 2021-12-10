alphabet = 'abcdefghjkmnpqrstuvwxyz'
password = 'hxbxwxba'

def increment(word):
    if word[-1] == 'z': return increment(word[:-1])+['a']
    else:
        word[-1] = alphabet[alphabet.index(word[-1])+1]
        return word
def nextPass(x):
    password = list(x)
    while True:
        password = increment(password)
        hasStraight = False
        for i in range(len(alphabet)-2):
            if alphabet[i:i+3] in ''.join(password):
                hasStraight = True
                break
        if not hasStraight: continue
        counter = 0
        for j in alphabet:
            counter += len(''.join(password).split(j+j))-1
        if counter > 1: break
    password = ''.join(password)
    return password

print(nextPass(password))
print(nextPass(nextPass(password)))
