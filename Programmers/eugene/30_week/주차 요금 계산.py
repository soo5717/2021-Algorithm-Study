import datetime

def solution(fees, records):
    answer = []
    
    base_time, base_fee, unit_time, unit_fee = fees
    cars_info, time_temp, cars_stat = dict(), dict(), dict()
    
    for record in records:
        _, car_number, _ = record.split(' ')
        cars_info[car_number] = 0

    for record in records:
        time, car_number, status = record.split(' ')
        cars_stat[car_number] = status
        
        if status == 'IN':
            time_temp[car_number] = time
            
        else:
            in_time = datetime.datetime.strptime(time_temp[car_number], "%H:%M")
            out_time = datetime.datetime.strptime(time, "%H:%M")
            time_interval = (out_time - in_time)
            
            cars_info[car_number] += time_interval.seconds//60
            
            
    for car_number, status in cars_stat.items():   
        if status == 'IN':
            in_time = datetime.datetime.strptime(time_temp[car_number], "%H:%M")
            out_time = datetime.datetime.strptime('23:59', "%H:%M")
            time_interval = (out_time - in_time)
            
            cars_info[car_number] += time_interval.seconds//60
            
    cars_info = sorted(cars_info.items(), key=lambda x : int(x[0]))

    for _, time in cars_info:
        unit = 0
        if time > base_time:
            unit = (time - base_time) // unit_time
            if (time - base_time) % unit_time:
                unit += 1
    
        total_fee = base_fee + unit * unit_fee
        answer.append(total_fee)
    
    return answer
