

for i in range(0,10):
    for j in range(0,i):
        for k in range(i,j):
            print(i,j)

for a in range(5):
    for b in range(2):
        print('foo')
    for x in range(a):
        for y in range(a-1):
            for z in range(y):
                print('bar')
