count = 0
num = 1
result = []

while count < 7:
    temp = num
    digits = str(num)
    power = len(digits)
    
    total = 0
    for d in digits:
        total += int(d) ** power
    
    if num % 2 != 0 and total == num: 
        result.append(num)
        count += 1
    
    num += 1

print(result)
