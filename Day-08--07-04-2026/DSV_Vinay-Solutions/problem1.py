#functions
def I():
    return(list(input()))


#Soln

t = int(input())
for _ in range(t):
    I()
    grid = []
    for i in range(8):
        tem = I()[:]
        grid.append(tem)
    
    # print(grid)

    ck = 0
    for i in range(8):
        for j in range(8):
            if j == 0:
                if grid[i][j] != 'R':
                    ck+=1
                    # print(i,j)
                    break
            else:
                if grid[i][j] != grid[i][j-1]:
                    # print(i,j)
                    ck+= 1
                    break
            
    if ck <8:
        print('R')
    else:
        print('B')
                    
        
            
