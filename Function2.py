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


