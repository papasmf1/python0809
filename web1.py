# web1.py 
#웹크롤링을 위한 선언
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#웹페이지 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체(html, xml)
soup = BeautifulSoup(page, "html.parser")
#전체 문서 보기
print( soup.prettify() )


