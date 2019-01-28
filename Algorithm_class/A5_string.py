# def strmp(s1, s2):
#     i=0
#     if len(s1) != len(s2):
#         return False
#     else:
#         while i<len(s1) and i<len(s2):
#             if s1[i] != s2[i]:
#                 return False
#             i += 1
#         return True
#
# def atoi(s):
#     value = 0
#     i =0
#     while(i < len(s)):
#         c = s[i]
#         # 아스키 코드 48 ~ 57 숫자
#         if c>='0' and c <='9':
#             digit = ord(c) - ord('0')
#         else:
#             break
#         value = (value*10) + digit;
#         i += 1
#     return value
#
# def itoa(n):
#     value = []
#     str =''
#     while n > 0:
#         num = n%10
#         value.append(num)
#         n //= 10
#     for i in value[::-1]:
#         ch = ord('0') + i
#         str += chr(ch)
#     return str
#
# print(itoa(123))
#
#
#
#
#
#
#
#


def Bbit_print(a):
    for i in range(7,-1,-1):
        if a&(1<< i):
            print(1, end='')
        else:
            print(0,end = '')

    print()

    a = 0xAA
    key = 0xAA
    print("a     ==>", end='')
    Bbit_print(a)
