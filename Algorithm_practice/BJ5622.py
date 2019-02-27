import sys
sys.stdin = open('input.txt')
nums = list(input())
num_dict = {}
flag = 0

num_dict = { str(i) : 0 for i in range(9)}
for num in nums:
    if num == '9' or num == '6':
        num_dict['6'] += 0.5
    else:
        num_dict[num] += 1


if num_dict['6']%1 == 0.5:
    num_dict['6'] += 0.5

print(int(max(num_dict.values())))
