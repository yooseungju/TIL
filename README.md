# 1218

###  파일 읽고 쓰기

#### - read
```python 
f = open("new.txt", "r") 
data = f.read()
print(data)
f.close()
```


#### - write
 - write a line
   

    ```python 
    # write() 이용하기
    with open("new.txt", "w", encoding='utf-8') as f:
    for i in range(1,101):
        data = f'{i} s번째 줄입니다.\n'
        f.write(data)
    ```

 - write lines

    ```python
    #writeslines() 이용하기
    menu = ["카레\t", "육개장\t", "순대강정\t"]

    with open("menu.txt", "w", encoding ='utf-8') as f:
        f.writelines(menu)
    ```



## Scrapting

```python
#import 중요 pip install 후 이용하기 
import requests
from bs4 import BeautifulSoup

req = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(req, 'html.parser')

#id값을 가져오는것이 가장 편함
kospi = soup.select_one("#KOSPI_now")

print(kospi.text)
```


- 실시간 검색어 긁어오기

```python 
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
hotkeyword = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > .ah_item")

for item in hotkeyword:
    print(item.select_one(".ah_r").text, end ='위  ')
    print(item.select_one(".ah_k").text)
```

   

# 1220

### - 딕셔너리 기초



