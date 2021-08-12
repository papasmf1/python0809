# DemoStr.py 

#print( dir(str) )

strData = "python is powerful"
print( strData.capitalize() )
print( strData.count("p") )
print( strData.count("p", 7) )
print( len(strData) )
print( "demo.ppt".endswith("ppt") )
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )

#공백문자 처리(전처리)
strB = "<<<  spam and ham  >>>"
print( strB )
result = strB.strip("<> ") 
print( result )
#치환
result = result.replace("spam", "spam egg")
#리스트로 받기
lst = result.split() 
print( lst )
#다시 하나의 문자열로 합치기 
print( ":)".join(lst) )



