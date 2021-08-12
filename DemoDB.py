# DemoDB.py 
import sqlite3

#연결객체를 리턴(일단은 메모리에 저장)
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\test2.db")

#구문을 실행하는 커서객체 리턴
cur = con.cursor()
#테이블 구조 만들기
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010');")

#파라메터 처리(별도의 입력 처리)
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber) )

#다중의 데이터를 입력(2차원 배열: 행과 열)
datalist = (("tom","010-123"), ("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist )

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

