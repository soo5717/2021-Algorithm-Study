def solution(places):
    answer = []
    
    for place in places:
        isRight = True
        test_place = []
        
        for n in place:
            test_place.append(list(n))
        
        for i in range(5):
            for j in range(5):
                if test_place[i][j] == "P":
                    if i + 1 < 5:
                        if test_place[i + 1][j] == "P":
                            isRight = False
                            break
                        if test_place[i + 1][j] == "O":
                            if i + 2 < 5:
                                if test_place[i + 2][j] == "P":
                                    isRight = False
                                    break
                    if j + 1 < 5:
                        if test_place[i][j + 1] == "P":
                            isRight = False
                            break
                        if test_place[i][j + 1] == "O":
                            if j + 2 < 5:
                                if test_place[i][j + 2] == "P":
                                    isRight = False
                                    break
                    if i + 1 < 5 and j + 1 < 5:
                        if test_place[i + 1][j + 1] == "P" and (test_place[i + 1][j] == "O" or test_place[i][j + 1] == "O"):
                            isRight = False
                            break
                    
                    if i + 1 < 5 and j - 1 >= 0:
                        if test_place[i + 1][j - 1] == "P" and (test_place[i + 1][j] == "O" or test_place[i][j - 1] == "O"):
                            isRight = False
                            break
        
        if isRight:
            answer.append(1)
        else:
            answer.append(0)

    return answer