# Function3.py
#합집합 문자를 리턴하는 함수(가변 인자를 처리)
def union(*ar):
    result = []
    # HAM(0) | EGG(1)
    for item in ar:
        # H(0) | A(1) | M(2)
        for x in item:
            if x not in result:
                result.append(x)
    return result

#함수 호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )

#필수와 옵션이 섞여 있는 경우(정의되지 않은 인자 처리)
#세번째부터는 딕셔너리 형태로 받겠다~~ 
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234") )
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234",
    name="mike", age="30") )

