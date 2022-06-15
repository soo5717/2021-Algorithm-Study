def make_star(points, x_points, y_points):
    x_min, x_max = min(x_points), max(x_points)
    y_min, y_max = min(y_points), max(y_points)
    
    matrix = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    
    for x, y in points:
        matrix[y_max - y][x - x_min] = '*'

    return [''.join(m) for m in matrix]

def solution(line):
    points = set()

    for i in range(0, len(line)):
        a, b, e = line[i]
        
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            
            denominator = a * d - b * c

            if denominator:
                x = (b * f - e * d) / denominator
                y = (e * c - a * f) / denominator

                if int(x) == x and int(y) == y:
                    points.add((int(x), int(y)))
                
    return make_star(points, list(zip(*points))[0], list(zip(*points))[1])