import numpy as np
import sys

n = int(input('Enter number of unknowns: '))
m = int(input("Enter number of equations:"))
a = np.zeros((m,n+1))
x = np.zeros(n)
for i in range(m):
    print("Equation",i+1)
    for j in range(n):
        print("Enter the coefficient of variable",j+1,":",end="")
        a[i][j] = float(input(""))
    k=j+1
    a[i][k]=float(input("Enter the constant:\n"))
print("Augmented matrix")
print(a)
for i in range(m):
    if a[i][i] == 0.0:
        for j in range(n):
            a[i][j]=a[i][j]+a[i+1][j]
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
print("REF matrix")
print(a)
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]

print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.3f' %(i+1,x[i]), end = '\t')

