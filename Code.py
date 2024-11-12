import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dimensions of the maze
N = 5

maze = np.array([
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1]
])
# Solution path
path = []

def is_safe(x, y):
    """ Check if (x, y) is a valid move in the maze """
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1

def solve_maze(x, y):
    """ Backtracking function to solve the maze """
    if x == N - 1 and y == N - 1:  # Destination reached
        path.append((x, y))
        return True

    if is_safe(x, y):
        path.append((x, y))  # Mark the path

        # Move down
        if solve_maze(x + 1, y):
            return True

        # Move right
        if solve_maze(x, y + 1):
            return True

        # Backtrack if neither down nor right leads to a solution
        path.pop()

    return False

# Initiate maze solving
if solve_maze(0, 0):
    print("Path found:", path)
else:
    print("No solution found.")

# Create a DataFrame for visualization
df = pd.DataFrame(maze)

# Mark the path on the maze
for (x, y) in path:
    df.iat[x, y] = 2  # Mark the path as '2' for visualization

# Plotting the maze
plt.figure(figsize=(6, 6))
plt.imshow(df, cmap='binary')  # Use a binary color map

# Mark the start point
plt.text(0, 0, 'S', ha='center', va='center', color='green', fontsize=20)  # Start
# Mark the end point
plt.text(N-1, N-1, 'E', ha='center', va='center', color='blue', fontsize=20)  # End

# Mark the path with red dots
for (x, y) in path:
    plt.text(y, x, '•', ha='center', va='center', color='red', fontsize=20)

plt.xticks([])  # Hide x ticks
plt.yticks([])  # Hide y ticks
plt.title("Maze Path Visualization")
plt.show()
