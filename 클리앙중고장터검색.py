# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식 사용 
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
#웹로봇을 금지하는 사이트 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우(대부분의 커뮤니티는 utf-8로 저장)
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <span class="subject_fixed" data-role="list-title-text">
        # 	아이패드 7세대 셀룰러 32기가 골드 팝니다(리퍼 신품)
        # </span>
        #<span 속성들... > 
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                try:
                        title = item.text 
                        if (re.search('맥북', title)):
                                print(title.strip())

                except:
                        pass
        
