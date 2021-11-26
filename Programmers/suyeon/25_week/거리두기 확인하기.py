from itertools import combinations

SPACE_SIZE = 5

def get_people(place):
    people = [] 
    for i in range(SPACE_SIZE):
        for j in range(SPACE_SIZE):
            if place[i][j] == 'P':
                people.append((i, j))
    return people

def is_succesful_distancing(place):
    for (r1, c1), (r2, c2) in combinations(get_people(place), 2):
        manhattan = abs(r1 - r2) + abs(c1 - c2)
        
        if manhattan > 2: 
            continue
        elif manhattan == 1:
            return False
            
        if r1 == r2:
            if place[r1][min(c1, c2) + 1] == 'X':
                continue
        elif c1 == c2:
            if place[min(r1, r2) + 1][c1] == 'X':
                continue
        else:
            r, c = min(r1, r2), min(c1, c2)
            if (r1 - r2) * (c1 - c2) > 0:
                if place[r][c + 1] == 'X' and place[r + 1][c] == 'X':
                    continue
            else:
                if place[r][c] == 'X' and place[r + 1][c + 1] == 'X':
                    continue
                    
        return False
    
    return True

def solution(places):
    return [ 1 if is_succesful_distancing(place) else 0 for place in places]