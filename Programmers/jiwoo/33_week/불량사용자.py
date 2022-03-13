from itertools import permutations 

def solution(user_id_s, banned_id_s):
    user_cases = list(permutations(user_id_s, len(banned_id_s)))
    answer = []

    for user_case in user_cases:
        if not check_banned_id(user_case, banned_id_s):
            continue
        else:
            user_case = set(user_case)
            if user_case not in answer:
                answer.append(user_case)

    return len(answer)

def check_banned_id(user_case, banned_id_s):
    for i in range(len(banned_id_s)):
        if len(user_case[i]) != len(banned_id_s[i]):
            return False

        for j in range(len(user_case[i])):
            if banned_id_s[i][j] == "*":
                continue
            if banned_id_s[i][j] != user_case[i][j]:
                return False
    return True