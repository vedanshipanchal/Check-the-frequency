test = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print("The original dict is:",test)


x = 2


count = 0
for key in test:
    if test[key]== x:
        count = count+1

print("Frequency is:",count)