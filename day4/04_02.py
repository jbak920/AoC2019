from itertools import groupby

def isNotDecreasing(digits):
    for i,digit in enumerate(digits[:-1]):
        if digit >digits[i+1]:
            return False
    return True

def hasSinglePair(digits):
    groups = [list(y) for x,y in groupby(digits)]
    for group in groups:
        if len(group) is 2:
            return True
    return False
    

def isValid(candidate):
    digits = [digit for digit in str(candidate)]
    if not isNotDecreasing(digits):
        return False
    return hasSinglePair(digits)

print '111111:', isValid(111111)
print '111122:', isValid(111122)
print '112233:', isValid(112233)
print '123444:', isValid(123444)
print '223450:', isValid(223450)
print '123789:', isValid(123789)

numValid = 0
minval = 240298
maxval = 784956
for candidate in range(minval, maxval+1):
    if isValid(candidate):
        numValid += 1

print numValid, "possible answers"