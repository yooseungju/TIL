import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())

    D = [list(map(int, input().split())) for _ in range(N)]

    cell = []
    cell_time = []
    cell_false = []

    for i in range(N):
        for j in range(M):
            if D[i][j]:
                cell.append((i,j))
                cell_time.append([D[i][j],D[i][j]])


    dy = (-1,1,0,0)
    dx = (0,0,-1,1)

    while K>0:
        cell_tmp = []
        cell_time_tmp = []

        i = 0


        while i < len(cell):
            x, y = cell[i]
            o = cell_time[i][0]
            z = cell_time[i][1]

            #활성화
            if z <= 0:
                for m in range(4):
                    nx = x + dx[m]
                    ny = y + dy[m]


                    if (nx,ny) not in cell_false:
                        if (nx,ny) not in cell_tmp:
                            cell_tmp.append((nx,ny))
                            cell_time_tmp.append([o,o])
                        else:
                            # 동시에 같은 곳에 접근할 때
                            index = cell_tmp.index((nx,ny))
                            if o > cell_time_tmp[index][0]:
                                cell_time_tmp[index]=[o,o]



            cell_time[i][1] -= 1

            #비활성화 시키기
            if -o == cell_time[i][1]:
                cell_false.append(cell[i])

                cell_time.pop(i)
                cell.pop(i)

            else:
                i += 1

        cell += cell_tmp
        cell_time += cell_time_tmp

        K-=1





    print(f"#{tc+1} {len(cell_time)}")