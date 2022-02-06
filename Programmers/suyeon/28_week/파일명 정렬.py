def file_split(file):
    head, number = '', 0
    
    for idx, token in enumerate(file):
        if token.isdigit():
            head = file[:idx]
            file = file[idx:]
            break
    
    number_flag = False
    for idx, token in enumerate(file):
        if not token.isdigit():
            number = file[:idx]
            number_flag = True
            break
    
    if not number_flag:
        number = file
        
    return (head.lower(), int(number))
    

def solution(files):
    file_dict = {file: file_split(file) for file in files}
    
    sorted_dict = dict(sorted(file_dict.items(), key=lambda x : (x[1][0], x[1][1])))
    
    return list(sorted_dict.keys())
