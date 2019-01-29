import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = '#' + input()
    data = [input() for i in range(100)]

    count = []
    c = 0

    # for p in range(100):
    #     # odd
    #     for j in range(1, 99):
    #         i = j - 1
    #         k = j + 1
    #         # 가로
    #         if data[p][i] == data[p][k]:
    #             count.append(3)
    #             if i == 0 or k == 99:
    #                 c += 1
    #             while (k < 99 and i > 0):
    #                 i -= 1
    #                 k += 1
    #                 if data[p][i] != data[p][k]:
    #                     c += 1
    #                     break
    #                 else:
    #                     count[c] += 2
    #         # 세로
    #         if data[i][p] == data[k][p]:
    #             count.append(3)
    #             if i == 0 or k == 99:
    #                 c += 1
    #             while (k < 99 and i > 0):
    #                 i -= 1
    #                 k += 1
    #                 if data[i][p] != data[k][p]:
    #                     c += 1
    #                     break
    #                 else:
    #                     count[c] += 2
    #
    #     # even
    #     for i in range(99):
    #         k = i + 1
    #         if data[p][i] == data[p][k]:
    #             count.append(2)
    #             if i == 0 or k == 99:
    #                 c += 1
    #             while (k < 99 and i > 0):
    #                 i -= 1
    #                 k += 1
    #                 if data[p][i] != data[p][k]:
    #                     c += 1
    #                     break
    #                 else:
    #                     count[c] += 2
    #         # 세로
    #         if data[i][p] == data[k][p]:
    #             count.append(2)
    #             if i == 0 or k == 99:
    #                 c += 1
    #             while (k < 99 and i > 0):
    #                 i -= 1
    #                 k += 1
    #                 if data[i][p] != data[k][p]:
    #                     c += 1
    #                     break
    #                 else:
    #                     count[c] += 2
    # print(tc, max(count))