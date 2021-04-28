def solution(phone_book):
    phone_book.sort()
    
    for i, phone in enumerate(phone_book[:-1]):
        if phone == phone_book[i+1][:len(phone)]:
            return False
    return True