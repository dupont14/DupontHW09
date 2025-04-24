def cb(num):    
    cube = num**3
    return cube
    
for x in range(19):
    if (x % 2) == 0:
        print(x)
    else:
        print(cb(x))
