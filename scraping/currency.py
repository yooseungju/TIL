import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
hotkeyword = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > .ah_item")

for item in hotkeyword:
    print(item.select_one(".ah_r").text, end ='위  ')
    print(item.select_one(".ah_k").text)

