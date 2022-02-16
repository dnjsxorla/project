import requests
import json
"""
작성 API URL

POST https://www.tistory.com/apis/post/write?
  access_token={access-token}
  &output={output-type}
  &blogName={blog-name}
  &title={title}
  &content={content}
  &visibility={visibility}
  &category={category-id}
  &published={published}
  &slogan={slogan}
  &tag={tag}
  &acceptComment={acceptComment}
  &password={password}


'access_token': ''
'blogName': 'revoltoso'


"""
access_token='e5c6a055ee27506ffa96947262aa791d_17046ffb71364dceb0565ffd5e464348'
URL = 'https://www.tistory.com/apis/post/write'

data = {
        'access_token': access_token,
        'blogName': 'revoltoso',
        'title': 'test_title',
        'visibility': '0',
        'category' : '990829'
        'content': 'test_content',
        'tag': 'test_tag',
    }

r = requests.post(URL, data=data)

print(r.text)


"""
# JSON 데이터 불러오기
with open('data18.json', 'r', encoding='UTF-8') as f:
    json_data = json.load(f)
f.close

# POST TISTORY
URL = 'https://www.tistory.com/apis/post/write'


test_data = {
    "킹덤 634화 (번역)": {
        "contents": [
            "킹덤",
            "634화",
            "(번역)"
        ],
        "link": "http://flash24.co.kr/g4/bbs/board.php?bo_table=cartoon&wr_id=8379&sca=&sfl=wr_subject&stx=%C5%B7%B4%FD&sop=and&page=2"
    }
}

for a in json_data:
    data = {
        'access_token': '83902dd4036b34f0413e1194a1fa4ea9_465acb2e765da62622e85eb403c4ee8a',
        'blogName': 'ditoon',
        'title': a,
        'visibility': '0',
        'category': '953206',
        'content': '<a href=\"' + json_data[a]['link'] + '\">' + a + '보기' + '</a>',
        'tag': '킹덤',
    }
    r = requests.post(URL, data=data)

"""
# taewonkim168 token = 83902dd4036b34f0413e1194a1fa4ea9_465acb2e765da62622e85eb403c4ee8a
# dnjsxorla token = 8df4a94033c3d64831e0dd8d61afb825_7482e0d89c0639c36f9b5ba29574010a


#access_token='3ccbda8cfbf39bdb8b7f0bf11af81c9d_2813231d5f039cc2759e21c9f386a6de'