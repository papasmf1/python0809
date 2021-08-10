# Function1.py 
#함수를 정의
def times(a,b):
    return a*b 

#함수를 호출 
#디버깅 모드로 실행(Break Point)
#논리적인 오류가 있는지를 찾는 경우 
print(times(5,6))

def setValue(newValue):
    x = newValue
    print("함수내부:",x)

#함수 호출
result = setValue(5)
print(result)

#함수를 정의
def swap(x,y):
    return y,x 

#호출
result = swap(3,4)
print(result[0])
print(result[1])

#입력된 단어의 문자 교집합 리턴 
def intersect(prelist, postlist):
    #지역변수를 초기화(교집합 문자 저장)
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#함수 호출
print( intersect("HAM","SPAM") )


