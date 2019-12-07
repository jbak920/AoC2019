def fuel(mass):
    this_fuel = int(int(mass) / 3) - 2
    if this_fuel > 0:
        return this_fuel + fuel(this_fuel)
    else:
        return 0
    
with open("inputs.txt") as f:
    data = f.readlines()

sum = 0
for mass in data:
    sum += fuel(mass)
    
print fuel(100756)
print sum