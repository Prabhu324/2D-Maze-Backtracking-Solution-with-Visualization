import time
from collections import deque
import numpy as np

# Sample Maze (1 represents open path, 0 represents walls)
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1]
]
start = (0, 0)
end = (4, 4)

# Utility Function to Print Solution Path
def print_solution(solution):
    for row in solution:
        print(row)
    print()

# 1. Backtracking Algorithm
def solve_maze_backtracking(maze, x, y, solution):
    if (x, y) == end:  # Reached the goal
        solution[x][y] = 1
        return True
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1:
        solution[x][y] = 1  # Mark as part of the path
        # Move Down
        if solve_maze_backtracking(maze, x + 1, y, solution):
            return True
        # Move Right
        if solve_maze_backtracking(maze, x, y + 1, solution):
            return True
        # Move Up
        if solve_maze_backtracking(maze, x - 1, y, solution):
            return True
        # Move Left
        if solve_maze_backtracking(maze, x, y - 1, solution):
            return True
        # Backtrack
        solution[x][y] = 0
    return False

# Run Backtracking and Measure Time
solution_bt = [[0] * len(maze[0]) for _ in range(len(maze))]
start_time = time.time()
backtrack_found = solve_maze_backtracking(maze, start[0], start[1], solution_bt)
bt_time = time.time() - start_time
print("Backtracking Solution:")
print_solution(solution_bt)
print(f"Backtracking Time: {bt_time:.6f} seconds\n")

# 2. BFS Algorithm
def solve_maze_bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    
    while queue:
        x, y = queue.popleft()
        solution[x][y] = 1
        if (x, y) == end:  # Reached the goal
            return solution, True
        # Explore neighbors
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return solution, False

# Run BFS and Measure Time
start_time = time.time()
solution_bfs, bfs_found = solve_maze_bfs(maze, start, end)
bfs_time = time.time() - start_time
print("BFS Solution:")
print_solution(solution_bfs)
print(f"BFS Time: {bfs_time:.6f} seconds\n")

# 3. DFS Algorithm
def solve_maze_dfs(maze, start, end):
    stack = [start]
    visited = set([start])
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    
    while stack:
        x, y = stack.pop()
        solution[x][y] = 1
        if (x, y) == end:  # Reached the goal
            return solution, True
        # Explore neighbors
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append((nx, ny))
    return solution, False

# Run DFS and Measure Time
start_time = time.time()
solution_dfs, dfs_found = solve_maze_dfs(maze, start, end)
dfs_time = time.time() - start_time
print("DFS Solution:")
print_solution(solution_dfs)
print(f"DFS Time: {dfs_time:.6f} seconds\n")

# Summary of Results
print("Algorithm Comparison:")
print(f"Backtracking - Path Found: {backtrack_found}, Time: {bt_time:.6f} seconds")
print(f"BFS - Path Found: {bfs_found}, Time: {bfs_time:.6f} seconds")
print(f"DFS - Path Found: {dfs_found}, Time: {dfs_time:.6f} seconds")
