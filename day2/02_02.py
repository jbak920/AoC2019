program = []
position = 0

def Opcode1():
    global program
    global position
    output = program[program[position + 1]] + program[program[position + 2]]
    program[program[position + 3]] = output
    position += 4

def Opcode2():
    global program
    global position
    output = program[program[position + 1]] * program[program[position + 2]]
    program[program[position + 3]] = output
    position += 4

def Intcode():
    global program
    global position
    while(True):
        opcode = program[position]
        if(opcode == 1):
            Opcode1()
        elif(opcode == 2):
            Opcode2()
        elif(opcode == 99):
            break
        else:
            print "Something went wrong at position", position
            break
    
with open("inputs.txt") as f:
    data = f.readline()
    
for entry in data.split(','):
    program.append(int(entry))


program[1] = 12
program[2] = 2

Intcode()

found = False

for noun in range(100):
    print noun
    for verb in range(100):
        position = 0
        program = []
        with open("inputs.txt") as f:
            data = f.readline()
            
        for entry in data.split(','):
            program.append(int(entry))


        program[1] = noun
        program[2] = verb

        Intcode()
        if (program[0] == 19690720):
            print noun, verb
            found = True
            break
    if(found):
        break
   
print program
    
