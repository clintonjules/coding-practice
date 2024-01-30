def displayPathtoPrincess(n,grid):
    mario = None
    peach = None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                mario = (i, j)
            
            elif grid[i][j] == 'p':
                peach = (i, j)
                
    mr = mario[0]
    mc = mario[1]
    pr = peach[0]
    pc = peach[1]
    
    # If neg, move up a row
    row_moves = pr - mr
    # If neg, move left a col
    col_moves = pc - mc
    
    for i in range(abs(row_moves)):
        if row_moves < 0:
            print("UP")
        else:
            print("DOWN")
            
    for j in range(abs(col_moves)):
        if col_moves < 0:
            print("LEFT")
        else:
            print("RIGHT")
