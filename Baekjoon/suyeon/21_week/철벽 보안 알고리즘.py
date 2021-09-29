import sys

input = sys.stdin.readline


def decrypt():
    public_key_dict = dict.fromkeys(public_key_2, 0)
    for idx, key in enumerate(public_key_1):
        public_key_dict[key] = idx

    decrypted_cryptogram = [''] * N
    for idx, value in enumerate(public_key_dict.values()):
        decrypted_cryptogram[value] = cryptogram[idx]
    return ' '.join(decrypted_cryptogram)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        public_key_1, public_key_2, cryptogram = input().split(), input().split(), input().split()
        print(decrypt())
