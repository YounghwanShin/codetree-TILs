def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    
    return max_area

def max_positive_rectangle(n, m, grid):
    heights = [0] * m
    max_area = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                heights[j] += 1
            else:
                heights[j] = 0
        max_area = max(max_area, largest_rectangle_area(heights))
    
    return max_area if max_area > 0 else -1

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = max_positive_rectangle(n, m, grid)
print(result)