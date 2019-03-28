T = int(input())

def div_class():
    N, K_min, K_max = map(int, input().split())
    score = list(input().split())
    score.sort()
    Min = 1000
    for t1 in range(1, N):
        for t2 in range(t1+1 , N):
            A = score[0:t1]
            B = score[t1:t2]
            C = score[t2:N]

            if K_min <= len(A) <= K_max and K_min <= len(B) <= K_max and K_min <= len(C) <= K_max:
                if len(set(score)) == len(set(A)) + len(set(B)) + len(set(C)):
                    if max(len(A), len(B), len(C)) - min(len(A), len(B), len(C)) < Min:
                        Min = max(len(A), len(B), len(C)) - min(len(A), len(B), len(C))

    if Min == 1000:
        return -1
    else:
        return Min



for tc in range(T):
    print(div_class())






