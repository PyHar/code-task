sum = ([i for i in range (20) if i % 4 == 0 or i % 7 == 0 ])


print (sum)
with open('output.txt', 'w') as f: 
    print( sum, file = f)