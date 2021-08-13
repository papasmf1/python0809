# Form2.py 
# Form2.ui(화면을 저장) + Form2.py(로직을 저장)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#미리 저장한 화면을 로딩(두번째 화면)
form_class = uic.loadUiType("form2.ui")[0]

#폼클래스 정의(QMainWindow 수정)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드 
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #슬롯메서드(시그널이 발생하면 자동 호출)
    def firstClick(self):
        self.label.setText("첫번째")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")


#직접 모듈을 실행했으면 실행
if __name__ == "__main__":
    #실행 프로세스를 생성 
    app = QApplication(sys.argv)
    #클래스의 인스턴스 생성
    demoWindow = DemoForm()
    #화면 보여주기 
    demoWindow.show()
    #계속 프로세스 대기중 
    app.exec_() 