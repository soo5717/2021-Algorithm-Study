def solution(w,h):
    return w * h - (w + h - gcd(w, h))


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
