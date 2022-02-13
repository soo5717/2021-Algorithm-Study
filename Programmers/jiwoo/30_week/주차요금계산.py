import math

def solution(fees, records):
    temp = []
    cars_times = dict()
    
    for i in range(len(records)):
        record_split = records[i].split(' ')
        temp.append(record_split)
        cars_times[record_split[1]] = 0
        temp[i][0] = [int(record_split[0][:2]), int(record_split[0][3:5])]
        
    for i in range(len(temp)):
        out = True
        if temp[i][2] != 'x':
            for j in range(i+1, len(temp)):
                if temp[j][2] != 'x':
                    if temp[i][1] == temp[j][1]:
                        minute = (temp[j][0][0] - temp[i][0][0]) * 60 + (temp[j][0][1] - temp[i][0][1])
                        temp[j][2], temp[i][2]='x', 'x'
                        cars_times[temp[i][1]] += minute
                        out = False
                        break
            if out:
                minute = (23 - temp[i][0][0]) * 60 + (59 - temp[i][0][1])
                cars_times[temp[i][1]] += minute

    for i, k in enumerate(cars_times):
        if cars_times[k] < fees[0]:
            cars_times[k] = fees[1]
        else:
            cars_times[k] = math.ceil((cars_times[k] - fees[0]) / fees[2]) * fees[3] + fees[1]
    return [cars_times[i] for i in sorted(cars_times)]