def solution(files):
    answer = []
    
    for file in files:
        head, number = '', ''
        for f in file:
            if f.isdigit():
                number += f
            elif number == '':
                head += f
            else:
                break
                
        answer.append((file, head.lower(), int(number)))
        
    answer.sort(key = lambda x: (x[1], x[2]))
    return [file[0] for file in answer]
