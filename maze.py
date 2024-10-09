import random

def generate_maze(width, height):
    # Adjust dimensions to be odd numbers
    if width % 2 == 0:
        width -= 1
    if height % 2 == 0:
        height -= 1

    # Initialize the maze with walls
    maze = [[0 for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]
    walls = []

    # Starting point
    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)

    maze[start_y][start_x] = 1
    visited[start_y][start_x] = True

    # Add the neighboring walls of the starting cell to the wall list
    walls.extend(get_walls(start_x, start_y, width, height, visited))

    while walls:
        # Pick a random wall from the list
        wx, wy, nx, ny = random.choice(walls)
        walls.remove((wx, wy, nx, ny))

        if not visited[ny][nx]:
            # Break the wall and mark the new cell as part of the maze
            maze[wy][wx] = 1
            maze[ny][nx] = 1
            visited[ny][nx] = True

            # Add the neighboring walls of the cell to the wall list
            walls.extend(get_walls(nx, ny, width, height, visited))

    # Adjust the maze to an 8x8 grid
    final_maze = adjust_maze(maze, 8, 8)
    return final_maze

def get_walls(x, y, width, height, visited):
    walls = []
    # Possible movements: up, down, left, right (in steps of 2)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Wall coordinates are between the current cell and the neighbor
        wx, wy = x + dx // 2, y + dy // 2

        if (0 < nx < width) and (0 < ny < height) and not visited[ny][nx]:
            walls.append((wx, wy, nx, ny))
    return walls

def adjust_maze(maze, target_width, target_height):
    # Add borders if necessary
    width = len(maze[0])
    height = len(maze)

    # Add horizontal borders
    while height < target_height:
        maze.insert(0, [0]*width)
        maze.append([0]*width)
        height += 2

    # Add vertical borders
    for row in maze:
        while len(row) < target_width:
            row.insert(0, 0)
            row.append(0)

    # Trim the maze to the target size
    return [row[:target_width] for row in maze[:target_height]]

# Generate an 8x8 maze
maze = generate_maze(8, 8)

# Print the maze as a list of lists
for row in maze:
    print(row)