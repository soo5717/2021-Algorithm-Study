from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answer = []
    info_dic = defaultdict(list)
    for info in infos:
        info = info.split()
        info_ = info[:-1]
        info_score = int(info[-1])
        
        # 가능한 info 조합 생성하여, key, score로 저장
        for i in range(5):
            for c in combinations(info_, i):
                temp_key = ''.join(c)
                info_dic[temp_key].append(info_score)
    
    # score 오름차순 정렬
    for key in info_dic.keys():
        info_dic[key].sort()
       
    for query in queries:
        query = query.split()
        query_score = int(query[-1])
        query_ = query[:-1]
        
        for i in range(3):
            query_.remove('and')
        while '-' in query_:
            query_.remove('-')
        query_ = ''.join(query_)
        
        if query_ in info_dic:
            scores = info_dic[query_]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start+end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid+1
                answer.append(len(scores)-start)
        else:
            answer.append(0)
    
    return answer