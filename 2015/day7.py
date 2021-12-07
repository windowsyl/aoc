data = open('day7input.txt', 'r').read().split('\n')[:-1]
data = [[int(i) if i.isnumeric() else i for i in j.split(' -> ')] for j in data]

commands = {}
values = {}

for line in data:
    if type(line[0]) is int: values[line[1]] = line[0]
    else: commands[line[1]] = line[0]

print(values)

while 'a' not in values:
    keysToPop = []
    for key in commands:
        command = commands[key].split()
        if command[0] == 'NOT' and command[1] in values:
            values[key] = 65535 ^ values[command[1]]
        elif command[0] in values:
            if len(command) == 1: # just x -> y
                values[key] = values[command[0]]
            elif command[2] in values:
                if command[1] == 'AND': values[key] = int(values[command[0]]) & int(values[command[2]])
                elif command[1] == 'OR': values[key] = int(values[command[0]]) | int(values[command[2]])
                else: print('aaaaaaaaaa')
            elif command[2].isnumeric(): #LSHIFT or RSHIFT
                if command[1] == 'LSHIFT': values[key] = values[command[0]] << int(command[2])
                elif command[1] == 'RSHIFT': values[key] = values[command[0]] >> int(command[2])
                else: print('bbbbbbbbbbbb')
        elif command[0] == '1' and command[2] in values: #only ever and apparently
            #print(command[1])
            values[key] = int(values[command[2]]) & 1
        if key in values: keysToPop.append(key)

    for key in keysToPop:
        print(key, '<-', commands[key])
        commands.pop(key)
        #print(commands)
print('p1:', values['a'])

data = open('day7input.txt', 'r').read().split('\n')[:-1]
data = [[int(i) if i.isnumeric() else i for i in j.split(' -> ')] for j in data]

commands = {}
values = {'b': values['a']}
for line in data:
    if type(line[0]) is int and line[1] != 'b': values[line[1]] = line[0]
    elif line[1] != 'b': commands[line[1]] = line[0]

while 'a' not in values:
    keysToPop = []
    for key in commands:
        command = commands[key].split()
        if command[0] == 'NOT' and command[1] in values:
            values[key] = 65535 ^ values[command[1]]
        elif command[0] in values:
            if len(command) == 1: # just x -> y
                values[key] = values[command[0]]
            elif command[2] in values:
                if command[1] == 'AND': values[key] = int(values[command[0]]) & int(values[command[2]])
                elif command[1] == 'OR': values[key] = int(values[command[0]]) | int(values[command[2]])
                else: print('aaaaaaaaaa')
            elif command[2].isnumeric(): #LSHIFT or RSHIFT
                if command[1] == 'LSHIFT': values[key] = values[command[0]] << int(command[2])
                elif command[1] == 'RSHIFT': values[key] = values[command[0]] >> int(command[2])
                else: print('bbbbbbbbbbbb')
        elif command[0] == '1' and command[2] in values: #only ever and apparently
            #print(command[1])
            values[key] = int(values[command[2]]) & 1
        if key in values: keysToPop.append(key)

    for key in keysToPop:
        #print(key, '<-', commands[key])
        commands.pop(key)
        #print(commands)
print('p2:', values['a'])