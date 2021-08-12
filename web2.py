# web2.py
#크롤링
from bs4 import BeautifulSoup
#웹서버와 통신
import urllib.request

#파일로 저장 
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for i in range(1,6):
    #동적으로 주소를 생성
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    #패키지명.모듈명.함수명()
    data = urllib.request.urlopen(url)
    #검색이 용이한 객체
    soup = BeautifulSoup(data, "html.parser")

    #블럭 주석: ctrl + / 
    # <td class="title">
    # 	<a href="/webtoon/detail">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
    # </td>
    cartoons = soup.find_all("td", class_="title")
    #갯수 출력
    print("갯수:{0}".format( len(cartoons) ))
    #슬라이싱 
    title = cartoons[0].find("a").text 
    link = cartoons[0].find("a")["href"]
    print(title)
    print(link)

    for item in cartoons:
        title = item.find("a").text 
        print( title.strip() )
        f.write( title.strip() + "\n" ) 

f.close() 



