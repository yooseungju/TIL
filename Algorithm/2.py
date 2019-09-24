import sys
sys.stdin = open('input.txt')
import itertools
M = [list(map(int, input().split()))]
N = int(input())

tmp = sorted(list(itertools.permutations(*M)))
print(''.join(map(str, tmp[N-1])))