num = 0x0269FAC9A0

D = int(hex(num),16)
B = bin(D)


pattern = ['001101', '010011', '111011',
           '110001', '100011', '110111',
           '001011', '111101', '011001',
           '101111']

B = str(B)
i = len(B)-1

A = []
flag = 1


while i > 2:
    if flag == 1:
        if B[i] =='1':
            A.append(0, B[i-5:i+1])
            flag = 0
    else:
        A.insert(0, B[i-5:i+1])
    i -= 5


print(B)
print(A)

