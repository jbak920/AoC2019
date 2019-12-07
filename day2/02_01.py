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
            print "Halting at opcode 99"
            break
        else:
            print "Something went wrong at position", position
            break
    print program
    
with open("inputs.txt") as f:
    data = f.readline()
    
for entry in data.split(','):
    program.append(int(entry))

program[1] = 12
program[2] = 2

Intcode()
print program