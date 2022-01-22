def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''

        is_number = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                is_number = True
            elif not is_number:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(parsing) for parsing in answer]