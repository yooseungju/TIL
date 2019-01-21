#
# arr  = [[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1]]
#
#
# result = 0
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         for m in range(4):
#             if j + dx[m] < 0 or i + dy[m] < 0:
#                 continue
#             elif j + dx[m] >= len(arr) or i + dy[m] >= len(arr):
#                 continue
#             else:
#                 r = abs(arr[i][j] - arr[i+dy[m]][j+dx[m]])
#                 result += r
#
# print(result)
#
#
#
# # 부분집합 만들기  -  1
# bit=[0,0,0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)
#
# # 부분집합 만들기  -  2
# arr = [1,2,3]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n+1):
#         if i&(i<<j):
#             print(arr[j], end=",")
#     print()
# print()



def subset(o_set):
    N = len(o_set)
    cnt = 0

    for i in range(1<<N):
        sum = 0
        for j in range(N+1):
            if i & (i<<j):
                sum += o_set[j]
    if sum == 0:
        cnt += 1
        for j in range(len(o_set)):
            if i&(1<<j):
                print(o_set[j], end =" ")
        print()



    return cnt




ans = subset([-7,-3,-2,5,8])
print(ans)




