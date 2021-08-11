#부모 클래스 정의 
class Person:
    #생성자 메서드 
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    #일반 인스턴스 메서드 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
        self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    #상속받은 생성자 메서드를 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모의 생성자 메서드를 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드 덮어쓰기(재정의)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
            self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject, 
            self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
#object클래스에서 제공하는 딕셔너리 어트리뷰트 
# print(p.__dict__)
# print(s.__dict__)
p.printInfo()
s.printInfo()


