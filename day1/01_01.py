def fuel(mass):
    return int(int(mass) / 3) - 2
    
with open("inputs.txt") as f:
    data = f.readlines()

sum = 0
for mass in data:
    sum += fuel(mass)
    
print sum