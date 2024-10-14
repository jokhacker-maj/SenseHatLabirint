import random

def generate_maze(width, height):
    # Initialize the maze with walls (1)
    maze = [[1 for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]
    walls = []

    # Starting point at (0, 0)
    start_x, start_y = 0, 0
    maze[start_y][start_x] = 0  # Mark the starting cell as a path
    visited[start_y][start_x] = True

    # Add the neighboring walls of the starting cell to the wall list
    walls.extend(get_walls(start_x, start_y, width, height, visited))

    while walls:
        # Pick a random wall from the list
        wx, wy, nx, ny = random.choice(walls)
        walls.remove((wx, wy, nx, ny))

        if not visited[ny][nx]:
            # Break the wall and mark the new cell as a path
            maze[wy][wx] = 0
            maze[ny][nx] = 0
            visited[ny][nx] = True

            # Add the neighboring walls of the cell to the wall list
            walls.extend(get_walls(nx, ny, width, height, visited))

    # Ensure the ending point at (7, 7) is a path
    maze[height - 1][width - 1] = 0

    # Optionally, connect the end point if it's isolated
    connect_end_point(maze, width, height)

    maze[7][-2] = 0
    return maze

def get_walls(x, y, width, height, visited):
    walls = []
    # Possible movements: up, down, left, right (in steps of 2)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Wall coordinates are between the current cell and the neighbor
        wx, wy = x + dx // 2, y + dy // 2

        if (0 <= nx < width) and (0 <= ny < height) and not visited[ny][nx]:
            walls.append((wx, wy, nx, ny))
    return walls

def connect_end_point(maze, width, height):
    x, y = width - 1, height - 1
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(neighbors)
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if maze[ny][nx] == 0:
                # Break the wall between (x, y) and (nx, ny)
                maze[(y + ny) // 2][(x + nx) // 2] = 0
                return

# Generate an 8x8 maze
maze = generate_maze(8, 8)

# Print the maze as a list of lists
for row in maze:
    print(row)