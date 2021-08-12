# DemoDB.py 
import sqlite3

#연결객체를 리턴(일단은 메모리에 저장)
con = sqlite3.connect(":memory:")
#구문을 실행하는 커서객체 리턴
cur = con.cursor()
#테이블 구조 만들기
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010');")
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

