# DemoRE.py 
#정규 표현식(특정한 규칙이 있는 패턴 검색)
import re 

print( re.search("[0-9]*th", "35th") )
print( re.match("[0-9]*th", "35th") )

result = re.search("[0-9]*th", "35th") 
print( result.group() )

#약간의 함정 추가
print( re.search("[0-9]*th", "  35th") )
#match함수는 정확하게 일치~~ 
print( re.match("[0-9]*th", "  35th") )

#단어 검색
print( re.search("apple", "this is apple") )
print( re.match("apple", "this is apple") )

#연도를 검색 
print( re.search("\d{4}", "올해는 2021년입니다.") )
#우편번호 
print( re.search("\d{5}", "우리 동네는 52300입니다.") )




