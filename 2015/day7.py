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
            if command[1] in values: # just x -> y
                values[key] = values[command[1]]
            elif command[2] in values:
                if command[1] == 'AND': values[key] = int(values[command[0]]) & int(values[command[2]])
                elif command[1] == 'OR': values[key] = int(values[command[0]]) | int(values[command[2]])
                else: print('aaaaaaaaaa')
            elif command[2].isnumeric(): #LSHIFT or RSHIFT
                if command[1] == 'LSHIFT': values[key] = values[command[0]] << int(command[2])
                elif command[1] == 'RSHIFT': values[key] = values[command[0]] >> int(command[2])
                else: print('bbbbbbbbbbbb')
        if key in values: keysToPop.append(key)

    for key in keysToPop:
        print(key, '<-', commands[key])
        commands.pop(key)
        #print(commands)
print(commands)