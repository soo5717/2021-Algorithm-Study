from math import ceil
from collections import defaultdict

LAST = 23 * 60 + 59


def time_converter(time):
    hour, minute = map(int ,time.split(':'))
    return hour * 60 + minute


def calculate_fee(fees, minute):
    base_minute, base_time, unit_time, unit_fee = fees 
    
    if minute <= base_minute:
        return base_time
    
    return base_time + ceil((minute - base_minute) / unit_time) * unit_fee


def solution(fees, records):
    car_dict = defaultdict(list)
    
    for record in records:
        time, car, io = record.split(' ')
        car_dict[car].append(time_converter(time))
    
    answer = []
    for car, record in car_dict.items():
        sum_time, record_length = 0, len(record)
        
        for idx in range(1, len(record), 2):
            sum_time += record[idx] - record[idx - 1]
            
        if record_length % 2 == 1:
            sum_time += LAST - record[-1]
        
        print(car, sum_time)
        answer.append((car, calculate_fee(fees, sum_time)))
        
    return list(zip(*sorted(answer)))[1]