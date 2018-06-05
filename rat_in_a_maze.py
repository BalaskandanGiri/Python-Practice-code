maze = [[1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 1]]
def find_path(i,j):
    if i==3 and j==3:
        maze[i][j]=2
        print(maze)
    elif maze[i][j]!=1:
        return
    else:
        maze[i][j]=2
        find_path(i,j+1)
        find_path(i+1,j)
        maze[i][j]=1
find_path(0,0)