import hmac
import hashlib
import binascii
import os
import time
import requests
import json
import urllib.parse

class Coupang:

#Coupang default value Access_ket and Secret_key and etc... 
    def __init__(self):
        self.access_key = 'X' 
        self.secret_key = 'X'
        self.subId = '' 
        self.method = 'GET' 
        self.DOMAIN = 'https://api-gateway.coupang.com' 

    def generateHmac(self, url): 
        path, *query = url.split("?")
        os.environ["TZ"] = "GMT+0"
        datetime = time.strftime('%y%m%d',time.gmtime()) + 'T' + time.strftime('%H%M%S',time.gmtime()) + 'Z'
        message = datetime + self.method + path + (query[0] if query else "")
        signature = hmac.new(bytes(self.secret_key, "utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(self.access_key, datetime, signature)

    def search_coupang(self, keyword):
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + keyword + "&limit=10" 
        url = "{}{}".format(self.DOMAIN, URL)
        response = requests.request(method=self.method, url=url, headers={"Authorization": self.generateHmac(URL),"Content-Type": "application/json;charset=UTF-8"})
        resdata = json.dumps(response.json(), indent=4, ensure_ascii=False)
        print(resdata)
        return 0


keyword = "ipad"
Coupang().search_coupang(keyword)