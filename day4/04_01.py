def isValid(candidate):
    digits = [digit for digit in str(candidate)]
    containsDouble = False
    for i,digit in enumerate(digits[:-1]):
        if digit >digits[i+1]:
            return False
        if digit == digits[i+1]:
            containsDouble = True
    
    return containsDouble
        
    

print '111111:', isValid(111111)        
print '223450:', isValid(223450)
print '123789:', isValid(123789)

numValid = 0
minval = 240298
maxval = 784956
for candidate in range(minval, maxval+1):
    if isValid(candidate):
        numValid += 1
        
print numValid, "possible answers"
