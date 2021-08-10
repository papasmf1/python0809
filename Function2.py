# Function2.py 
#불변형식 연습
a = 1.2 
print( id(a))
a = 2.3 
print( id(a))

print("----가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#가변형식이 대부분(List)
wordlist = ["J","A","M"]

#함수 정의
def change(x):
    #복사본을 생성(깊은복사)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

#함수 호출
change(wordlist)
print("함수 호출후:", wordlist)


#이름해석규칙(LGB)
x = 1 
def func(a):
    return a+x 

#호출
print( func(1) )

def func2(a):
    x = 2 
    return a+x 

#호출 
print( func2(1) )

#기본값
def times(a=10,b=20):
    return a*b 

#호출 
print( times() )
print( times(5) )
print( times(b=3) )
print( times(3,4) )

#키워드 인자(파라메터명 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="8080", server="credu.com") )
