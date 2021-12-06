import hashlib
for i in range(10000000):
    s = 'ckczppom' + str(i)
    x = hashlib.md5(s.encode())
    if x.hexdigest()[0:5] == '00000':
        print('day 1', i)
        if x.hexdigest()[0:6] == '000000':
            print('day 2', i)
            exit()

