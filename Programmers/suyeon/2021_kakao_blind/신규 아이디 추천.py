import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = re.sub("[^a-z0-9-_.]", "", new_id) # 2단계
    new_id = re.sub("[.]+", ".",new_id) # 3단계
    new_id = re.sub("^[.]|[.]$", "", new_id) # 4단계
    if not new_id: new_id = "a" # 5단계
    new_id = re.sub("[.]$", "", new_id[:15]) # 6단계
    if len(new_id) <= 2: new_id = new_id.ljust(3, new_id[-1]) # 7단계
        
    return new_id