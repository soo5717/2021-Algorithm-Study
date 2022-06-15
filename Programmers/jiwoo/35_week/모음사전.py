def solution(word):
    word_list = []
    
    word_list = make_word(0, word_list, "")
 
    return word_list.index(word) + 1

def make_word(count, word_list, new_word):
    if count == 5:
        return
    
    words = "AEIOU"

    for i in range(len(words)):
        word_list.append(new_word + words[i])
        make_word(count + 1, word_list, new_word + words[i])
            
    return word_list