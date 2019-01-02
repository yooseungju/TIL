"""
파이썬 dictionary 기초
"""


#1.  평균을 구하세요.

# score = { "국어": 87,
#          "영어": 92,
#          "수학": 40

# }

# hab = 0
# avg = 0
# for v in score.values():
#         hab += v
#         avg = hab / len(score)
# print("평균값: " , avg)

# print(sum(score.values())/len(score))

# 2. 반 평균을 구하시오

# scores = {
#         "철수":{ 
# 			"국어": 80,
# 			"음악": 90,
# 			"수학": 100 
#         },

#         "영희":{ 
# 			"국어": 70,
# 			"음악": 60,
# 			"수학": 50
#         }               
# }

# hab = 0
# count = 0
# for k in scores.keys():
# 	for v in scores[k].values():
#         hab += v
#         count += 1

# print(hab/count)

#3. 도시 주에 최근 3일 중 가장 추웠던 곳, 가장 더웠던 곳은?

cities = {
	"서울" : [-6,-10,5],
	"대전": [-3,-5,2],
	"광주": [0,-2,10],
	"부산": [2,-2,9]
}

# high = {}
# low = {}

# for k, v in cities.items():
# 	high[k] = max(v)
# 	low[k] = min(v)

# for k , v in high.items():
# 	if v == max(high.values()):
# 		print(k)

# for k , v in low.items():
# 	if v == min(low.values()):
# 		print(k)

max_temp = 0
min_tamp = 0

max_area = ""
min_area = ""

for k, v in cities.items():
	if max_temp < max(v):
		max_temp = max(v)
		max_area = k
	
	if min_tamp > min(v):
		min_tamp = min(v)
		min_area = k

print("가장 더운지역:",max_area)
print("가장 추운지역:",min_area)










