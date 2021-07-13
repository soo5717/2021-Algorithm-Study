def solution(N, stages):
    answer = []
    result={}
    
    for i in range(1,N+2): result[i] =0
    for stage in stages: result[stage]+=1
    
    for i in range(1,N+1):
        stage_num,noclear=0,0
        for j in range(i,N+2) :
            stage_num+=result[j]   
        noclear= result[i]
        answer+= [(i,noclear/stage_num)] if stage_num else [(i,0)]
        
    answer=sorted(answer, key=lambda x:x[1], reverse=True)
    return [k[0] for k in answer]
