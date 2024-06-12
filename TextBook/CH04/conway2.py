import random, time, copy
WIDTH = 60
HEIGHT = 20


next_cells = []
for y in range(HEIGHT):
    raw = [] 
    for x in range(WIDTH):
        if random.randint(0, 1) == 0:
            raw.append('#')
        else:
            raw.append(' ') 
    next_cells.append(raw) 

while True: 
    print('\n\n\n\n\n') 
    current_cells = copy.deepcopy(next_cells)

    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[y][x], end='')
        print() 

    
    for y in range(HEIGHT):
        for x in range(WIDTH):
     
          
            left_coord  = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            
            num_neighbors = 0
            if current_cells[above_coord][left_coord] == '#':
                num_neighbors += 1 
            if current_cells[above_coord][x] == '#':
                num_neighbors += 1
            if current_cells[above_coord][right_coord] == '#':
                num_neighbors += 1
            if current_cells[y][left_coord] == '#':
                num_neighbors += 1 
            if current_cells[y][right_coord] == '#':
                num_neighbors += 1 
            if current_cells[below_coord][left_coord] == '#':
                num_neighbors += 1 
            if current_cells[below_coord][x] == '#':
                num_neighbors += 1
            if current_cells[below_coord][right_coord] == '#':
                num_neighbors += 1 

           
            if current_cells[y][x] == '#' and (num_neighbors == 2 or num_neighbors == 3):
              
                next_cells[y][x] = '#'
            elif current_cells[y][x] == ' ' and num_neighbors == 3:
               
                next_cells[y][x] = '#'
            else:
                
                next_cells[y][x] = ' '
    time.sleep(1) 
