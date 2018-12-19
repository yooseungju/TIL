# item = int(input(" 번호를 입력하세요 "))
# for i in range(1, item+1):
#     print(i)


# warn_investment_list= ['microsoft','google', 'naver','kakao', 'samsung', 'lg']
# print(f'경고종목 리스트:{warn_investment_list}')
# item = input('what is your investment?:  ')

# if item in warn_investment_list:
#     print("투자 경고 종목입니다.")


# colors = ['Apple' , 'Banana', 'Coconut', 'Deli', 'Ele','Grape']
# newlist = []
# index = 0

# for i in colors:
#     if index not in [0, 4, 5]:
#         newlist.append(i)
#     index= index+1
# print(newlist)


ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])

