import random
import requests
import json
from pprint import pprint
import re

# 0. random 로또 번호 생성
# 1. api를 통해 우승 번호를 가져온다.
# 2. 0과 1를 비교하여 등수를 알려준다.




 

p = re.compile(r'[drwtNo]\d+')
set1 = set()
bonus = 0

for k, v in lotto.items():
    if p.findall(k):
        set1.add(v)
    elif k == "firstPrzwnerCo":
        bonus = v

count = 0

while True:
    count+=1
    set2 = set(random.sample(range(1,46),6))

    if len(set1 & set2) == 3:
        pass
    elif len(set1 & set2) == 4:
        pass
    elif len(set1 & set2) == 5:
        if bonus in set2:
            print("2등2등2등2등2등2등2등")
            print(count,"000원")
        else:
            print("3등3등3등")
    elif len(set1 & set2) == 6:
        print("1등")
        print(count, "000원")
        break
    

