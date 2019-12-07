from copy import copy

class Circuit:
    def __init__(self):
        self.end_= [0,0] #[x,y]
        self.path_ = set(tuple([]))
        self.longPath_ = []

    def AddToPath(self, dir, distance):
        if dir == 'R':
            for i in range(distance):
                self.end_[0] += 1
                self.path_.add(tuple(self.end_))
                self.longPath_.append(copy(self.end_))
        if dir == 'L':
            for i in range(distance):
                self.end_[0] -= 1
                self.path_.add(tuple(self.end_))
                self.longPath_.append(copy(self.end_))
        if dir == 'U':
            for i in range(distance):
                self.end_[1] += 1
                self.path_.add(tuple(self.end_))
                self.longPath_.append(copy(self.end_))
        if dir == 'D':
            for i in range(distance):
                self.end_[1] -= 1
                self.path_.add(tuple(self.end_))
                self.longPath_.append(copy(self.end_))
        
    def SortPath(self):
        temp = [list(t) for t in list(set([tuple(entry) for entry in self.path_]))]
        temp.sort();
        self.path_ = temp

circuit1 = Circuit()
circuit2 = Circuit()


    
# Example 1:
# data1 = 'R8,U5,L5,D3'
# data2 = 'U7,R6,D4,L4'
    
# Example 2
# data1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# data2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

# Example 3
# data1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
# data2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

with open("inputs.txt") as f:
    data1 = f.readline()
    data2 = f.readline()

for stretch in data1.split(','):
    dir = stretch[0]
    distance = int(stretch[1:])
    circuit1.AddToPath(dir, distance)
    
for stretch in data2.split(','):
    dir = stretch[0]
    distance = int(stretch[1:])
    circuit2.AddToPath(dir, distance)
    
common = circuit1.path_ & circuit2.path_
closest = sorted(common, key=lambda common: (abs(common[0])+abs(common[1])))

intersectionDict = {}

for steps,position in enumerate(circuit1.longPath_):
    if(tuple(position) in common):
        intersectionDict[tuple(position)] = steps +1
        
for steps,position in enumerate(circuit2.longPath_):
    if(tuple(position) in common):
        intersectionDict[tuple(position)] += steps +1

earliest = min(intersectionDict, key=intersectionDict.get)
earliest_steps = intersectionDict[earliest]
    
    
print "Closest:", list(closest)[0]
print "Earliest:", earliest, "with", earliest_steps, "steps"

