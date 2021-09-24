import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        words_line = int(input())
        key1, key2, cypher = input().split(), input().split(), input().split()
        rel = dict((key2[i], cypher[i]) for i in range(words_line))

        array=[]
        for i in key1:
            array.append(rel[i])
        print(' '.join(array))
