def solution(phone_book):
    #sorted로 정렬하면 phone_book에 있는 원소들은 앞자리가 작은 순서로 정렬된다.
    #앞 뒤로 비교하기만 하면 되는 것!
    
    #sorted를 해주지 않으면, 모든 조합에 대해 살펴봐야 하고 효율성에 적합하지 않다.
    phoneBook = sorted(phone_book)
    
    for pre, phone in zip(phoneBook, phoneBook[1:]):
        if phone.startswith(pre):
            return False
    return True
