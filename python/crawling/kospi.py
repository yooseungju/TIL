# import requests
# from bs4 import BeautifulSoup
# req = requests.get("https://www.google.com")
# print(req)
# print(req.text)
# print(req.status_code)
# print(req.json())

# # soup = BeautifulSoup(req, 'html.parser')
# # kospi = soup.status_code('경로')
# # req = requests.get("https://www.naver.com/")


# url = "https://finance.naver.com/sise/"
# req = requests.get(url).text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#KOSPI_now")

# print("현재 코스피 지수는 ", kospi.text)





import requests
import json

url = 'https://api.github.com/'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.text)
print(response.json())