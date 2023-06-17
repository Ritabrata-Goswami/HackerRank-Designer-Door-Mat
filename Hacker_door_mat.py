N,M = input().split()   #variable input. 

c='.|.'
N=int(N)  #casting both variables into int.
M=int(M)
thickness=int((N-1)/2)  #Number of rows without middle row i.e. 'WELCOME' row.

#Printing the upper half
for i in range(thickness):
    print((((c*i).rjust(thickness*3,'-'))+c+((c*i).ljust(thickness*3,'-'))))

print('WELCOME'.center(M,'-'))  #Middle row

#Printing the lower half
for i in range(thickness,0,-1):
    print((((c*(i-1)).rjust(thickness*3,'-'))+c+((c*(i-1)).ljust(thickness*3,'-'))))
