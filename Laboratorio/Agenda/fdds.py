import random
Y = [[0]*4]*3
X = [[ random.randint (1,100) for i in range(3)] for j in range(4)]
print('Y1:',Y)
print('X1:',X)
for i in range( len (X)):
    for j in range( len (X[0])):
        Y[j][i] = X[i][j]

print('Y2:',Y)
print('X2:',X)
