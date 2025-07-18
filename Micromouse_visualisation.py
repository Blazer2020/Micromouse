import copy 

def print_maze(maze):    
    for i in range(len(maze)):
        if i%2 == 0:
            for j in range(len(maze[i])):
                try:
                    if maze[i][2*j] == "!":
                        print("o", end="")
                    elif maze[i][2*j] == "o":
                        print("·", end="")
                except:
                    pass
                try:
                    if maze[i][2*j+1] == "!":
                        print("----", end="")
                    elif maze[i][2*j+1] == "o":    
                        print("    ", end="")
                except:
                    pass
            print()
        elif i%2 == 1:
            for j in range(len(maze[i])):
                try:
                    if maze[i][2*j] == "!":
                        print("|", end="")
                    elif maze[i][2*j] == "o":
                        print(" ", end="")
                except:
                    pass
                try:
                    if maze[i][2*j+1] == "o":
                        print("    ", end="")
                    else:
                        if len(str(maze[i][2*j+1])) == 1:
                            print("  "+str(maze[i][2*j+1])+" ", end="")
                        elif len(str(maze[i][2*j+1])) == 2:
                            print(" "+str(maze[i][2*j+1])+" ", end="")

                except:
                    pass
            print()

def floodfill(maze,r,c,n,z):
    global maze_path
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if type(maze[i][j]) == int:
                maze[i][j] = "o"
    
    
    if z==0:
        maze[15][15] = 0
        maze[15][17] = 0
        maze[17][15] = 0
        maze[17][17] = 0
        process_queue = []
        process_queue.extend([(15,15),(15,17),(17,15),(17,17)])
    elif z==1:
        maze[31][1] = 0
        process_queue = []
        process_queue.extend([(31,1)])
    #print(process_queue)
    


    while len(process_queue)>0:
        check_walls(process_queue[0][0],process_queue[0][1],maze)
        replace_val(process_queue[0][0],process_queue[0][1],maze[process_queue[0][0]][process_queue[0][1]]+1,process_queue,blocked,maze)
        process_queue.pop(0)
    #print(process_queue)
    #print_maze(maze)
    maze_path = copy.deepcopy(maze)
    maze_path[r][c] = "#"

def replace_val(r,c,n,list,blocked,maze):
    if "t" not in blocked:
        try:
            if maze[r-2][c] == "o":
                maze[r-2][c] = n
                list.append((r-2,c))
        except:
            pass
    if "r" not in blocked:
        try:
            if maze[r][c+2] == "o":
                maze[r][c+2] = n
                list.append((r,c+2))
        except:
            pass
    if "b" not in blocked:
        try:
            if maze[r+2][c] == "o":
                maze[r+2][c] = n
                list.append((r+2,c))
        except:
            pass
    if "l" not in blocked:
        try:
            if maze[r][c-2] == "o":
                maze[r][c-2] = n
                list.append((r,c-2))
        except:
            pass

def check_walls(r,c,maze):
    global blocked
    blocked = []
    try:
        if maze[r-1][c] == "!":
            blocked.append("t")
    except:
        pass
    try:
        if maze[r][c+1] == "!":
            blocked.append("r")
    except:
        pass
    try:
        if maze[r+1][c] == "!":
            blocked.append("b")
    except:
        pass
    try:
        if maze[r][c-1] == "!":
            blocked.append("l")
    except:
        pass
    #print("blocked####################: ",blocked)
    return blocked

def set_Walls(r,c,maze):
    for i in blocked:
        if i == "t":
            maze[r-1][c-1] = "!"
            maze[r-1][c] = "!"
            maze[r-1][c+1] = "!"
        if i == "r":
            maze[r-1][c+1] = "!"
            maze[r][c+1] = "!"
            maze[r+1][c+1] = "!"
        if i == "b":
            maze[r+1][c-1] = "!"
            maze[r+1][c] = "!"
            maze[r+1][c+1] = "!"
        if i == "l":
            maze[r-1][c-1] = "!"
            maze[r][c-1] = "!"
            maze[r+1][c-1] = "!"
    
def next_cell(r,c,maze):
    n = maze[r][c]
    global next_val
    next_val = []
    #print(maze[r][c])
    try:
        if maze[r-2][c] == n-1 and maze[r-1][c] == "o":
            next_val.append([r-2,c])
            print("T")
    except:
        pass
    try:
        if maze[r][c+2] == n-1 and maze[r][c+1] == "o":
            next_val.append([r,c+2])
            print("R")
    except:
        pass
    try:
        if maze[r+2][c] == n-1 and maze[r+1][c] == "o":
            next_val.append([r+2,c])
            print("B")
    except:
        pass
    try:    
        if maze[r][c-2] == n-1 and maze[r][c-1] == "o":
            next_val.append([r,c-2])
            print("L")
    except:   
        pass
    print(next_val)

def select_cell(r0,c0,r1,c1,list):
    global r
    global c
    global last_cell
    selected_somehting = False
    #moving up
    if r0 == r1-2 and c1==c0:
        if [r1-2,c1] in list:
            last_cell = [r1,c1]
            r = r1-2
            c = c1
            selected_somehting = True

    #moving right
    if r0 == r1 and c1==c0+2:
        if [r1,c1+2] in list:
            last_cell = [r1,c1]
            r = r1
            c = c1+2
            selected_somehting = True

    #moving left
    if r0 == r1 and c1==c0-2:
        if [r1,c1-2] in list:
            last_cell = [r1,c1]
            r = r1
            c = c1-2
            selected_somehting = True
    
    #moving down
    if r0 == r1+2 and c1==c0:
        if [r1+2,c1] in list:            
            last_cell = [r1,c1]
            r = r1+2
            c = c1
            selected_somehting = True

    if not(selected_somehting):
        last_cell = [r1,c1]
        #considering start cell is bottom right corner change this to whatever start cell is dummy
        if list[0][0] != list[1][0]:
            if 31-list[0][0] > 31-list[1][0]:
                r = list[1][0]
                c = list[1][1]
            else:
                r = list[0][0]
                c = list[0][1]
        elif list[0][1] != list[1][1]:
            if list[0][1]-1 > list[1][1]-1:
                r = list[1][0]
                c = list[1][1]
            else:
                r = list[0][0]
                c = list[0][1]
        
def move_to_goal():
    z = 0  # while going to goal z = 0; while coming back z = 1
    global r
    global c
    global last_cell
    r = 31
    c = 1
    n = 1
    goal_reached = False
    last_cell = [r, c]
    
    while not goal_reached:
        check_walls(r, c, maze1)
        set_Walls(r, c, maze_empty)
        floodfill(maze_empty, r, c, n, z)
        print_maze(maze_path)
        print("last cell : ", last_cell)

        next_cell(r, c, maze_empty)
        if len(next_val) > 1:
            select_cell(last_cell[0], last_cell[1], r, c, next_val)
            print("next cell is: ", r, c)
        else:
            last_cell = [r, c]
            r = next_val[0][0]
            c = next_val[0][1]
            print("next cell is: ", r, c)

        n += 1

        if (r == 15 and c == 15 or r == 15 and c == 17 or r == 17 and c == 15 or r == 17 and c == 17):
            goal_reached = True
            check_walls(r, c, maze_empty)
            set_Walls(r, c, maze_empty)
            floodfill(maze_empty, r, c, n, z)
            print_maze(maze_path)
            print("You reached the goal!")


maze_empty = [
    
    ["!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 2
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 3
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 4
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 5
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 6
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 7
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 8
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 9
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!""o"
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!""!"
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"2
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"3
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"4
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"5
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"6
    ["!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!"],#wall
]

maze1 = [
    
    ["!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!"],#wall
    ["!", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"
    ["!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!"],#wall
    ["!", "o", "!", "o", "!", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 2
    ["!", "o", "!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!"],      #cell 3
    ["!", "!", "!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "o", "o", "!", "!", "!", "!", "!", "!", "!", "!", "o", "o", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "!", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!"],      #cell 4
    ["!", "o", "!", "!", "!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "o", "!", "!", "!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!"],      #cell 5
    ["!", "o", "!", "!", "!", "!", "!", "o", "!", "o", "!", "o", "!", "!", "!", "o", "!", "!", "!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!"],      #cell 6
    ["!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "o", "o", "o", "o", "!", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!"],      #cell 7
    ["!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!", "!", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!"],      #cell 8
    ["!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "o", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!"],#wall
    ["!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell 9
    ["!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "o", "!", "o", "!", "!", "!", "!", "!", "o", "!", "o", "!", "!", "!", "o", "!", "!", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!"],      #cell "!""o"
    ["!", "o", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!", "!", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "o", "o", "o", "o", "!", "o", "!"],      #cell "!""!"
    ["!", "o", "!", "!", "!", "!", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"2
    ["!", "o", "!", "!", "!", "o", "!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "!", "o", "!", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!"],      #cell "!"3
    ["!", "!", "!", "o", "!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!", "o", "!"],#wall
    ["!", "o", "o", "o", "o", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!", "o", "!"],      #cell "!"4
    ["!", "o", "!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!"],#wall
    ["!", "o", "!", "o", "!", "o", "o", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"5
    ["!", "o", "!", "o", "!", "o", "!", "o", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "o", "!"],#wall
    ["!", "o", "!", "o", "!", "o", "!", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "!"],      #cell "!"6
    ["!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!", "!"],#wall
]


def next_cell_coming_back(r,c,maze):
    n = maze[r][c]
    global next_val
    next_val = []
    print(maze[r][c])
    try:
        if maze[r-2][c] == n-1 and maze[r-1][c] == "o":
            next_val.append([r-2,c])
            print("T")
    except:
        pass
    try:
        if maze[r][c+2] == n-1 and maze[r][c+1] == "o":
            next_val.append([r,c+2])
            print("R")
    except:
        pass
    try:
        if maze[r+2][c] == n-1 and maze[r+1][c] == "o":
            next_val.append([r+2,c])
            print("B")
    except:
        pass
    try:    
        if maze[r][c-2] == n-1 and maze[r][c-1] == "o":
            next_val.append([r,c-2])
            print("L")
    except:   
        pass
    print(next_val)

def move_to_start():
    z=1
    global r
    global c
    global last_cell
    n=1
    goal_reached = False
    while not(goal_reached):
        check_walls(r,c,maze1)
        set_Walls(r,c,maze_empty)
        floodfill(maze_empty,r,c,n,z)        
        print_maze(maze_path)
        print("last cell : ",last_cell)
        next_cell_coming_back(r,c,maze_empty)
        if len(next_val) > 1:
            select_cell(last_cell[0],last_cell[1],r,c,next_val)
            print("next cell is: ",r,c)
        else:
            last_cell = [r,c]
            r = next_val[0][0]
            c = next_val[0][1] 
            print("next cell is: ",r,c)
        n += 1
        if (r==31 and c==1):
            goal_reached = True
            check_walls(r,c,maze1)
            set_Walls(r,c,maze_empty)
            floodfill(maze_empty,r,c,n,z)        
            print_maze(maze_path)

move_to_goal()
move_to_start()
move_to_goal()
#print_maze(maze1)