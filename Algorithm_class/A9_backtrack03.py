def process_solution(a,k):
    for i in range(1, k+1):
        print(data[a[i]], end = '')
    print()

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1,k):
        in_perm[a[i]] = True

    ncands = 0

    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k ==input:
        process_solution(a, k)

    else:
        k+=1
        ncands = make_candidates(a, k ,input, c)
