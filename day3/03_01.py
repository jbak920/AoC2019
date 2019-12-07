from copy import copy

class Circuit:
    def __init__(self):
        self.end_= [0,0] #[x,y]
        self.path_ = set(tuple([]))

    def AddToPath(self, dir, distance):
        if dir == 'R':
            for i in range(distance):
                self.end_[0] += 1
                self.path_.add(tuple(self.end_))
        if dir == 'L':
            for i in range(distance):
                self.end_[0] -= 1
                self.path_.add(tuple(self.end_))
        if dir == 'U':
            for i in range(distance):
                self.end_[1] += 1
                self.path_.add(tuple(self.end_))
        if dir == 'D':
            for i in range(distance):
                self.end_[1] -= 1
                self.path_.add(tuple(self.end_))
        
    def SortPath(self):
        temp = [list(t) for t in list(set([tuple(entry) for entry in self.path_]))]
        temp.sort();
        self.path_ = temp

circuit1 = Circuit()
circuit2 = Circuit()

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
print list(closest)[0]
