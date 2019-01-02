from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800,838), 8)
for num in numbers:

    req = requests.get("https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="+str(num)).text
    soup = BeautifulSoup(req, 'html.parser')

    temp  = soup.select_one(".win_result")
    lottolist = temp.select(".num.win  .ball_645")
    bonus = temp.select_one(".num.bonus  .ball_645").text

    print("\n< ",num,"> 회 당첨 번호")
    for i in lottolist:
        print(i.text, end=" ")
    print(" + ", bonus)
    
