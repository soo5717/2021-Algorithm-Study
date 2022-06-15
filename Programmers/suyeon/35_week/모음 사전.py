from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    words = []
    for i in range(len(vowels)):
        words.extend(map(''.join, list(product(vowels, repeat = i + 1))))
    
    return sorted(words).index(word) + 1