import requests
import sys
import datetime
import json
from urllib.request import Request, urlopen
import csv
import os
import pprint
from bs4 import BeautifulSoup
import urllib.request





all_of_data_01 = {}


key = os.environ['KEY']


def project_01():
    now = datetime.datetime.now()
    date = now.replace(day=13)

    for _ in range(0,10):
            s_date = date.strftime("%Y%m%d")
            url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={s_date}&weekGb=0'

            req= Request(url)
            res = urlopen(req)
    
            res_body = res.read()
            res_json = json.loads(res_body)

        
            for j in range(0,10):
                k_mv_code = res_json['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieCd']

                if k_mv_code not in all_of_data_01.keys():
                    all_of_data_01[k_mv_code] = [
                        res_json['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieNm'],
                        res_json['boxOfficeResult']['weeklyBoxOfficeList'][j]['audiAcc'], s_date]
                
            date = date - datetime.timedelta(days=7)

    with open('boxoﬃce.csv ', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movie_code','title','audience','recorded_at')

        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()

        for k, v in all_of_data_01.items():
            writer.writerow({'movie_code':k,'title':v[0],'audience':v[1],'recorded_at':v[2]})


def project_02():
    all_of_data_02 = {}
    mv_cd_list =[]
    with open('boxoﬃce.csv', 'r', encoding='utf-8') as f:
        items = csv.reader(f)
        
        for item in items:
            mv_cd_list.append(item[0])

    
    del mv_cd_list[0]
 
            

    

    for k in mv_cd_list:
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={k}"
        req= Request(url)
        res = urlopen(req)
        res_body = res.read()
        res_json = json.loads(res_body)
    

        mv_info_dict = res_json["movieInfoResult"]["movieInfo"]

       

        all_of_data_02[k] = [mv_info_dict['movieNm'], 
                            mv_info_dict['movieNmEn'],
                            mv_info_dict['movieNmOg'],
                            mv_info_dict['openDt'],
                            mv_info_dict['showTm'],
                            [v['genreNm'] for v in mv_info_dict['genres']],
                            mv_info_dict['directors'][0]['peopleNm'],
                            mv_info_dict['audits'][0]['watchGradeNm'],
                            [v['peopleNm'] for v in mv_info_dict['actors']]
                            ]

    print(all_of_data_02)

  

    with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movie_code','movieNm','movieNmEn','movieNmOg','openDt','showTm','genres','directors','watchGradeNm','actor_01','actor_02','actor_03')

        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()


        for k, v in all_of_data_02.items():
            actors = v[8]
            actor_01 = ''
            actor_02 = ''
            actor_03 = ''
        

            for i, vv in enumerate(actors):
                if i == 0:
                    actor_01 = vv
                elif i == 1:
                    actor_02 = vv
                elif i == 3:
                    actor_03 = vv

            writer.writerow({'movie_code':k,
            'movieNm':v[0],
            'movieNmEn':v[1],
            'movieNmOg':v[2],
            'openDt':v[3],
            'showTm':v[4],
            'movieNmOg':' '.join(v[5]), 
            'directors':v[6],
            'watchGradeNm':v[7],
            'actor_01': actor_01,
            'actor_02': actor_02,
            'actors_03': actor_03})


def project_03():
    naver_client_id = os.environ['NAVER_KEY_ID']
    naver_client_secret = os.environ['NAVER_KEY_Secret']
    mv_name_list =[]
    mv_code_list=[]
    all_of_data_03 = {}


    with open('movie.csv', 'r', encoding='utf-8') as f:
        items = csv.reader(f)
        
        for item in items:
            mv_name_list.append(item[1])
            mv_code_list.append(item[0])
    
    del mv_name_list[0]
    del mv_code_list[0]


    for index, mv_name in enumerate(mv_name_list):
        url = f'https://openapi.naver.com/v1/search/movie.json?query={mv_name}'
        headers = {
            'X-Naver-Client-Id': naver_client_id,
            'X-Naver-Client-Secret': naver_client_secret
        }

        res_json = requests.get(url, headers=headers).json()

        all_of_data_03[mv_code_list[index]] = [res_json['items'][0]['image'],
                                                res_json['items'][0]['link'],
                                                res_json['items'][0]['userRating']]


    with open('movie_naver.csv ', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movie_code','thumbnail','link','userRating')

        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()

        for k, v in all_of_data_03.items():
            writer.writerow({'movie_code':k,'thumbnail':v[0],'link':v[1],'userRating':v[2]})


def project_04():
    mv_code_list=[]
    mv_image_list=[]
    with open('movie_naver.csv', 'r', encoding='utf-8') as f:
        items = csv.reader(f)
        
        for item in items:
            mv_code_list.append(item[0])
            mv_image_list.append(item[1])


        del mv_code_list[0]
        del mv_image_list[0]
    

    print(mv_code_list)
    print(mv_image_list)

    for index, image in enumerate(mv_image_list):
        file = urllib.request.urlopen(image).read()
        name = mv_code_list[index]+'jpg'

        with open(f"images/{name}", mode="wb") as f:
            f.write(file)
            print("finish...")



project_01()
project_02()
project_03()
project_04()