#-*-coding:utf-8-*-

import hmac
import hashlib
import binascii
import os
import time
import requests
import json
import urllib.parse
from ast import literal_eval

class Coupang:

#Coupang default value Access_ket and Secret_key and etc... 
    def __init__(self):
        self.access_key = 'X' 
        self.secret_key = 'X'
        self.subId = 'AF8339687' 
        self.method = 'GET' 
        self.limit = '3'
        self.DOMAIN = 'https://api-gateway.coupang.com' 
        
    def generateHmac(self, url): 
        path, *query = url.split("?")
        os.environ["TZ"] = "GMT+0"
        datetime = time.strftime('%y%m%d',time.gmtime()) + 'T' + time.strftime('%H%M%S',time.gmtime()) + 'Z'
        message = datetime + self.method + path + (query[0] if query else "")
        signature = hmac.new(bytes(self.secret_key, "utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(self.access_key, datetime, signature)

    def search_coupang(self, keyword):
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + keyword + "&limit=" + self.limit + "&subId=" + self.subId
        url = "{}{}".format(self.DOMAIN, URL)
        response = requests.request(method=self.method, url=url, headers={"Authorization": self.generateHmac(URL),"Content-Type": "application/json;charset=UTF-8"})
        resdata = json.dumps(response.json(), indent=4, ensure_ascii=False)
        #print(resdata)
        return resdata

    def best_categories_coupang(self, Id):
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/bestcategories/"+ Id + "?limit=" + self.limit + "&subId=" + self.subId
        url = "{}{}".format(self.DOMAIN, URL)
        #print(url)
        response = requests.request(method=self.method, url=url, headers={"Authorization": self.generateHmac(URL),"Content-Type": "application/json;charset=UTF-8"})
        resdata = json.dumps(response.json(), indent=4, ensure_ascii=False)
        #print(resdata)
        return resdata

    def goldbox_coupang(self):
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/goldbox"+ "?subId=" + self.subId
        url = "{}{}".format(self.DOMAIN, URL)
        #print(url)
        response = requests.request(method=self.method, url=url, headers={"Authorization": self.generateHmac(URL),"Content-Type": "application/json;charset=UTF-8"})
        resdata = json.dumps(response.json(), indent=4, ensure_ascii=False)
        #print(resdata)
        return 0

    def create_data(self, contents):
        now_time = time.time()
        tm = time.strftime('%Y-%m-%d_%I%M%S',time.localtime(now_time))
        file_name = 'Data\\' + str(tm) + '.csv'
        
        with open(file_name,'w',encoding='utf-8') as f:
            f.write(contents)
        return 0

################### Categories ####################

#1001   여성패션
#1002	남성패션
#1010	뷰티
#1011	출산/유아동
#1012	식품
#1013	주방용품
#1014	생활용품
#1015	홈인테리어
#1016	가전디지털
#1017	스포츠/레저
#1018	자동차용품
#1019	도서/음반/DVD
#1020	완구/취미
#1021	문구/오피스
#1024	헬스/건강식품
#1025	국내여행
#1026	해외여행
#1029	반려동물용품
#1030	유아동패션
###################################################


category_list = ["1001","1010","1016","1017","1018","1019"]


#/products/goldbox
keyword_origin = '샤프'
keyword = urllib.parse.quote(keyword_origin)

Id = "1001"
#data = Coupang().search_coupang(keyword)
data_str = Coupang().best_categories_coupang(Id)
#Coupang().goldbox_coupang()
data_json = json.loads(data_str)
Coupang().create_data(str(data_json['data']))