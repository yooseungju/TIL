N = int(input())

cnt = 0

for i in range(N):
    for j in range(N):
        if ((i+1)**2) + ((j+1)**2) > (N**2):
            cnt+=1
print(((N*N)-cnt)*4)


