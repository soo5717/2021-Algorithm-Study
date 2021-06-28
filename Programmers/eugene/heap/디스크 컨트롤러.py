import heapq
def solution(jobs):
    sumtime,end=0,0
    heap=[]
    
    len_jobs=len(jobs)
    heapq.heapify(jobs)

    while(jobs or heap):
        #대기가 있는지 확인
        temp=list(jobs)
        for job in jobs: 
            if job[0]<= end: 
                temp.remove(job)
                heapq.heappush(heap,[job[1], job[0]])
        jobs=temp

        if(heap==[]):
            end = jobs[0][0]
        else : #제일 짧은 수행시간의 일을 먼저 수행
            run = heapq.heappop(heap)
            end+=run[0] 
            sumtime= sumtime+end-run[1]
    return sumtime //len_jobs
