import sys
sys.stdin = open('input.txt')

T = int(input())

def ans():
    num = int(input())

    matrix = [list(map(int, input().split())) for _ in range(num)]



for tc in range(T):
    print(f'{tc+1} {ans()}')