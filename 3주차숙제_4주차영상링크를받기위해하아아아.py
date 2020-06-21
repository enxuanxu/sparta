import requests
from bs4 import BeautifulSoup
 
if __name__ == "__main__":
    RANK = 50 ## 차트 순위가 1 ~ 50위까지 있음
 
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1](https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers = header) ## 주간 차트를 크롤링 할 것임
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')
 
    titles = parse.find_all("div", {"class": "ellipsis rank01"}) 
    singers = parse.find_all("div", {"class": "ellipsis rank02"}) 
    albums = parse.find_all("div",{"class": "ellipsis rank03"})
 
    title = []
    singer = []
    album = []
 
    for t in titles:
        title.append(t.find('a').text)
 
    for s in singers:
        singer.append(s.find('span', {"class": "checkEllipsis"}).text)

    for a in albums:
        album.append(a.find('a').text)
 
    for i in range(RANK):
        print('%3d위: %s [ %s ] - %s'%(i+1, title[i], album[i], singer[i]))
