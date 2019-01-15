import sys
sys.stdin = open("flatten.txt")
T = 10



def flatten():
    num = int(input())
    block_list =  list(map(int, input().split()))

    for i in range(num):

        Min = block_list[0]
        Min_index = 0
        Max = block_list[0]
        Max_index = 0

        for index, value in enumerate(block_list):
            if Min > value:
                Min = value
                Min_index = index
                continue

            elif Max < value:
                Max = value
                Max_index = index

        block_list[Min_index] += 1
        block_list[Max_index] -= 1

    m_in = block_list[0]
    m_ax = block_list[0]

    for i in block_list[1:]:
        if i < m_in:
            m_in =i
            continue
        elif i > m_ax:
            m_ax = i



    return (m_ax- m_in)

for tc in range(T):
    print("#{} {}".format(tc+1, flatten()))
