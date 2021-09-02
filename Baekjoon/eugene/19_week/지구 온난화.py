if __name__ == "__main__":
    R, C = map(int, input().split())
    
    mapInfo=['.'*(C+2)]
    for _ in range(R):
        mapInfo.append('.'+input()+'.')  
    mapInfo.append('.'*(C+2))
 
    answer = mapInfo[:]
    x_start, x_end = R+10, 0
    y_start, y_end = C+10, 0
    for x in range(1,R+1):
        for y in range(1,C+1):
            if mapInfo[x][y] == 'X':
                cnt=0
                if mapInfo[x-1][y] =='.': cnt+=1
                if mapInfo[x][y-1] =='.': cnt+=1
                if mapInfo[x][y+1] =='.': cnt+=1
                if mapInfo[x+1][y] =='.': cnt+=1

                if cnt >= 3:
                    answer[x]=str(answer[x][:y]+answer[0][0]+answer[x][y+1:])
                else :
                    x_start, x_end = min(x, x_start), max(x, x_end)
                    y_start, y_end = min(y, y_start), max(y,y_end)

    for x_idx in range(x_start, x_end+1):
        print(answer[x_idx][y_start:y_end+1])
