import itertools


r, c, num = map(int, input().split())
matrix = []

for _ in range(r):
    matrix.append(list(itertools.accumulate(map(int, input().split()))))

# for i in range(r):
#     for j in range(1 ,c):
#         matrix[i][j] += matrix[i][j-1]
#
for i in range(1,r):
    for j in range(0, c):
        matrix[i][j] += matrix[i-1][j]

for _ in range(num):
    hab = 0
    ai, aj, bi, bj = map(int, input().split())
    ai, aj, bi, bj = ai-1, aj-1, bi-1, bj-1

    if ai == 0 and aj == 0:
        hab = matrix[bi][bj]
    elif ai == 0:
        hab = matrix[bi][bj] - matrix[bi][aj - 1]
    elif aj == 0:
        hab = matrix[bi][bj] - matrix[ai - 1][bj]
    else:
        hab = matrix[bi][bj] - matrix[ai-1][bj] - matrix[bi][aj-1] + matrix[ai-1][aj-1]
    print(hab//((bi-ai+1)*(bj-aj+1)))


#
# R, C, Q = map(int, input().split())
#
# psum = [[0 for cols in range(C + 1)] for rows in range(R + 1)]
#
# for r in range(1, R + 1):
#     cols = list(map(int, input().split()))
#     for c in range(1, C + 1):
#         psum[r][c] = cols[c - 1] + psum[r - 1][c] + psum[r][c - 1] - psum[r - 1][c - 1]
#
# for q in range(Q):
#     r1, c1, r2, c2 = map(int, input().split())
#
#     sum = psum[r2][c2] - psum[r1 - 1][c2] - psum[r2][c1 - 1] + psum[r1 - 1][c1 - 1]
#     n = (r2 - r1 + 1) * (c2 - c1 + 1)
#
#     print(sum // n)





