def rule_check(room):
    manhattan = [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (0, -1), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0) ]
    
    for x, info in enumerate(room):
        for y, i in enumerate(info):
            if i == 'P':
                for (mx, my) in manhattan:
                    nx = x + mx
                    ny = y + my
                    
                    if nx < 0 or ny < 0 or nx >= 5 or ny >=5:
                        continue
                        
                    if room[nx][ny] == 'P': #거리두기 실패. 그러나 파티션 확인해보기
                        if (abs(mx) + abs(my) == 1): # 거리 1 : 상하좌우(파티션 고려X)
                            return 0
                        else : #거리 2
                            if not mx or not my: # 상하좌우로 거리 2
                                if mx > 0: cx = x+1
                                elif mx < 0: cx = x-1
                                else: cx = x
                                    
                                if my > 0: cy = y+1
                                elif my < 0: cy = y-1
                                else: cy = y
                                
                                if room[cx][cy] == 'O':
                                    return 0
                                
                            else: # 대각선 거리 2
                                if room[x][ny] == 'O' or room[nx][y] =='O':
                                    return 0
    return 1

def solution(places):
    result = []
    for p in places:
        result += {rule_check(p)}
    return result
