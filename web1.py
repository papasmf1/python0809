# web1.py 
#웹크롤링을 위한 선언
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#웹페이지 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체(html, xml)
soup = BeautifulSoup(page, "html.parser")
#전체 문서 보기
#print( soup.prettify() )

#<p>태그 전부 검색 ==> 리스트 객체로 리턴 
#print( soup.find_all("p") )

#<p> 하나 
#print( soup.find("p") )

#특정 스타일을 검색(필터링하는 조건)
#<p class="outer-text">컨텐츠</p>
#print( soup.find_all("p", class_="outer-text") )

#id를 지정(유니크한 이름)
#print( soup.find_all(id="first") )

#태그 안쪽에 있는 컨텐츠 
for item in soup.find_all("p"):
    #text속성을 지정 
    title = item.text.replace("\n", "")
    title = title.replace("\t", "")
    print( title.strip() )





