import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
from datetime import datetime
import pyqtgraph as pg

class MyFrame(QtWidgets.QFrame):
    def __init__(self, parent=None,initials=None):
           QtWidgets.QFrame.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
           self.table = QtWidgets.QTableWidget(25,3,self)
           self.table.move(65,0)
           self.table.resize(450,1200)

           #text input - 출생연도
           text, ok = QInputDialog.getText(self, '출생연도', '본인의 출생연도를 입력하세요\n (예 : 1962년생 -> "1962" 입력)')
           currentYear = datetime.now().year

           # 조기/연기 연금 선택하기
           pension_type= ("조기 연금","연기 연금")
           pension_type, ok = QInputDialog.getItem(self,"조기/연기 연금", "(조기/연기) 원하시는 연금 종류를 선택하세요", pension_type, 0, False)

           # ----------------------------------- 조기 연금 선택시 --------------------------------------------------------
           if pension_type == "조기 연금":
                   #text input - 연금액
                   pension1, done1 = QtWidgets.QInputDialog.getText(
                       self, '연금액', '본인의 예상 연금액을 입력하세요 (월 단위)\n (예 : 100만원(한 달 기준) -> "100" 입력)')
                   if pension1 and done1:
                       pension1_float = float(pension1)*12
                       #pension1 초기화값 - 비교시 필요
                       pension1_ini = float(pension1)*12
                       print("본인 연금액",pension1)

                   #text input - 몇 년치 연금
                   how, done2 = QtWidgets.QInputDialog.getText(
                       self, '조기 연금 년도', '몇 년을 미리 받고 싶으십니까 ?\n (예 : 2년 미리 연금 수령 -> "2" 입력)')
                   if how and done2:
                       how_int=int(how)
                       print("몇 년치 ?",how)
                       if how_int == 0:
                           msg = QMessageBox()
                           msg.setWindowTitle("조기 연금 계산기")
                           msg.setText("이 프로그램은 조기 연금 계산기입니다. \n반드시  조기 연금 년도를 선택하셔야 합니다.")
                           msg.exec_()
                           sys.exit()
                       if int(text) <=1952:
                                year = str(60-how_int)
                                print(year)
                       elif int(text) >=1953 and int(text) <=1956:
                                year = str(61-how_int)
                                print(year)
                       elif int(text) >=1957 and int(text) <=1960:
                                year = str(62-how_int)
                                print(year)
                       elif int(text) >=1961 and int(text) <=1964:
                                year = str(63-how_int)
                                print(year)
                       elif int(text) >=1965 and int(text) <=1968:
                                year = str(64-how_int)
                                print(year)
                       else :
                                year = str(65-how_int)
                                print(year)

                   # 가장 왼쪽에 나이별로 나오는 부분
                   for i in range(0, 30):
                       y = str(int(year) + i)
                       x = QtWidgets.QTableWidgetItem(y)
                       x.setBackground(QtGui.QColor(0, 0, 255))
                       self.table.setVerticalHeaderItem(i, x)

                   #text input - 조기 연금을 선택했을 시, 접수한 시기에 정해진 기본 연금액 기입
                   pension2, done3 = QtWidgets.QInputDialog.getText(
                       self, '변경된 연금액', '본인의 변경된 연금액을 입력하세요 (월 단위)\n조기 연금 신청한 시기에 다시 정해진 기본 연금액 기입 (예 : 95만원(한 달 기준) -> "95" 입력)')
                   if pension2 and done3:
                       pension2_float = float(pension2)*(1-0.06*how_int)*12
                       #pension2 초기화값 - 비교시 필요
                       pension2_ini = float(pension2)*(1-0.06*how_int)*12
                       print("변경된 연금액",pension2)
                       print(pension2_float)

                   # 조기연금
                   item1 = QtWidgets.QTableWidgetItem('조기연금')
                   item1.setBackground(QtGui.QColor(255, 0, 0))
                   self.table.setHorizontalHeaderItem(0, item1)

                   pension2=str(round(pension2_float,0))
                   pension0=pension2 # 이렇게하면 pension0값은 상수로 사용할 수 있음
                   pension2_graph=pension2 #그래프 사용할 때 필요한 변수
                   self.table.setItem(0,0,QTableWidgetItem(pension2)) #조기연금 가장 처음 값
                   for i in range (0,25):
                       pension2_float = round(float(pension0)*(i+2),0) #조기연금의 n 배 = n년차
                       pension2=str(pension2_float)
                       self.table.setItem(1+i,0,QTableWidgetItem(pension2))

                   # 노령연금
                   item2 = QtWidgets.QTableWidgetItem('노령연금')
                   item2.setBackground(QtGui.QColor(0, 255, 0))
                   self.table.setHorizontalHeaderItem(1,item2)

                   pension1=str(pension1_float)
                   pension0=pension1 # 이렇게하면 pension0값은 상수로 사용할 수 있음
                   for i in range (1,30):
                       pension1_float = float(pension0)*i
                       pension1=str(pension1_float)
                       self.table.setItem(i-1+how_int,1,QTableWidgetItem(pension1))

                   # pension1(노령)&pension2(조기) 초기화
                   # 조기 & 노령연금 비교
                   for i in range(how_int,29+how_int):
                         pension1_float = float(pension1_ini)*(i-how_int+1)
                         pension2_float = round(float(pension2_ini),0)*(i+1)
                         print("노령연금 :",pension1_float)
                         print("조기연금 :",pension2_float)
                         print("-----------------------")

                         if pension1_float > pension2_float:
                             print("---------------------------")
                             print("노령연금이 조기연금보다 더 클 때")
                             print("노령연금",pension1_float)
                             print("조기연금",pension2_float)
                             z=int(year)+i
                             print("그 때 나이 : ",z,"세")
                             z=str(z)
                             x = QtWidgets.QTableWidgetItem(z)
                             x.setBackground(QtGui.QColor(255, 0, 0))
                             self.table.setVerticalHeaderItem(i, x)
                             break

                   # 연기 연금
                   item3 = QtWidgets.QTableWidgetItem('연기연금')
                   item3.setBackground(QtGui.QColor(255, 196, 0))
                   self.table.setHorizontalHeaderItem(2,item3)

                   # 그래프 그리기

                   age_pension2 = range(int(year),int(year)+27) # 조기 연금 나이

                   n = list(range(0,int(year)*2)) # (노령연금) 범위까지 x값은 아무 의미없는 값으로 설정 -> 그래프에 표시하기 위함
                   for i in range(int(year)+1, int(year)*2):
                       n[i] = float(pension0)*(i-int(year)-(how_int-1)) # 해당 나이에 받는 연금(누적액)

                   m = list(range(0,int(year)*2)) # (조기연금) 범위까지 x값은 아무 의미없는 값으로 설정 -> 그래프에 표시하기 위함
                   for i in range(int(year), int(year)*2):
                       m[i] = float(pension2_graph)*(i-int(year)+1)

                   plt = pg.plot()
                   plt.setXRange(age_pension2[0],age_pension2[26])
                   plt.setLimits(xMin=age_pension2[0], xMax=age_pension2[26])
                   plt.setLimits(yMin=0)
                   plt.setGeometry(25,25,1000,500)
                   plt.setWindowTitle('조기 및 노령 연금 비교 그래프')
                   plt.addLegend()

                   c1=plt.plot(m,pen='r', name='조기 연금')
                   c2=plt.plot(n,pen='g', name='노령 연금')
                   c3=plt.addLine(x=z,pen=(0,0,255))

           # ----------------------------------- 연기 연금 선택시 --------------------------------------------------------
           else:
               # 연기 연금
               item3 = QtWidgets.QTableWidgetItem('연기연금')
               item3.setBackground(QtGui.QColor(255, 196, 0))
               self.table.setHorizontalHeaderItem(2,item3)

               # 노령연금
               item2 = QtWidgets.QTableWidgetItem('노령연금')
               item2.setBackground(QtGui.QColor(0, 255, 0))
               self.table.setHorizontalHeaderItem(1, item2)

               # text input - 연금액
               pension1, done1 = QtWidgets.QInputDialog.getText(
                   self, '연금액', '본인의 예상 연금액을 입력하세요 (월 단위)\n (예 : 100만원(한 달 기준) -> "100" 입력)')
               if pension1 and done1:
                   pension1_float = float(pension1) * 12
                   # pension1 초기화값 - 비교시 필요
                   pension1_ini = float(pension1) * 12
                   print("본인 연금액", pension1)

               # text input - 몇 년치 연금
               how, done2 = QtWidgets.QInputDialog.getText(
                   self, '연기 연금 년도', '몇 년 뒤에 받고 싶으십니까 ?\n (예 : 2년 뒤에 연금 수령 -> "2" 입력)')
               if how and done2:
                   how_int = int(how)
                   print("몇 년치 ?", how)
                   if how_int == 0:
                       msg = QMessageBox()
                       msg.setWindowTitle("연기 연금 계산기")
                       msg.setText("이 프로그램은 연기 연금 계산기입니다. \n반드시 연기 연금 년도를 선택하셔야 합니다.")
                       msg.exec_()
                       sys.exit()
                   if int(text) <= 1952:
                       year = str(60 + how_int)
                       print(year)
                   elif int(text) >= 1953 and int(text) <= 1956:
                       year = str(61 + how_int)
                       print(year)
                   elif int(text) >= 1957 and int(text) <= 1960:
                       year = str(62 + how_int)
                       print(year)
                   elif int(text) >= 1961 and int(text) <= 1964:
                       year = str(63 + how_int)
                       print(year)
                   elif int(text) >= 1965 and int(text) <= 1968:
                       year = str(64 + how_int)
                       print(year)
                   else:
                       year = str(65 + how_int)
                       print(year)

               #색깔넣기
               for i in range(0, 30):
                   y = str(int(year)-how_int + i)
                   x = QtWidgets.QTableWidgetItem(y)
                   x.setBackground(QtGui.QColor(0, 0, 255))
                   self.table.setVerticalHeaderItem(i, x)

               #text input - 연기 연금을 선택했을 시, 원금에 퍼센트를 합침 (pension3 - 연기 연금)

               pension3 = float(pension1) * (1 + 0.072 * how_int) * 12

               #pension3 초기화값 - 비교시 필요

               pension3_ini = pension3
               pension3_float = pension3

               pension3 = str(round(pension3, 0))
               pension0 = pension3  # 이렇게하면 pension0값은 상수로 사용할 수 있음
               pension3_graph = pension3 #그래프 사용할 때 필요한 변수
               pension3_first = self.table.setItem(how_int, 2, QTableWidgetItem(pension3))  # 연기연금 가장 처음 값

               for i in range(0, 25):
                   pen3 = round(float(pension0) * (i + 2), 0)  # 조기연금의 n 배 = n년차
                   pension3 = str(pen3)
                   self.table.setItem(1 + i + how_int, 2, QTableWidgetItem(pension3))

               #text input - 연기 연금을 선택했을 시, 접수한 시기에 정해진 기본 연금액 기입
               pension2, done3 = QtWidgets.QInputDialog.getText(
                   self, '변경된 연금액', '본인의 변경된 연금액을 입력하세요 (월 단위)\n연기 연금 신청한 시기에 다시 정해진 기본 연금액 기입 (예 : 105만원(한 달 기준) -> "105" 입력)')
               if pension2 and done3:
                   pension2_float = float(pension2)*(1+0.072*how_int)*12
                   #pension2 초기화값 - 비교시 필요
                   pension2_ini = float(pension2)*(1+0.072*how_int)*12
                   print("변경된 연금액",pension2)
                   print(pension2_float)

               # 노령연금
               item2 = QtWidgets.QTableWidgetItem('노령연금')
               item2.setBackground(QtGui.QColor(0, 255, 0))
               self.table.setHorizontalHeaderItem(1, item2)

               pension1 = str(pension1_float)
               pension0 = pension1  # 이렇게하면 pension0값은 상수로 사용할 수 있음
               for i in range(1, 26+how_int):
                   pension1_float = float(pension0) * (i-how_int)
                   pension1 = str(pension1_float)
                   self.table.setItem(i - 1 - how_int, 1, QTableWidgetItem(pension1))

               # 조기연금 이름만 나오게 함
               item1 = QtWidgets.QTableWidgetItem('조기연금')
               item1.setBackground(QtGui.QColor(255, 0, 0))
               self.table.setHorizontalHeaderItem(0, item1)

               # pension1(노령)&pension3(연기) 초기화
               # 연기 & 노령연금 비교
               for i in range(how_int, 29 + how_int):
                   pension1_float = float(pension1_ini) * (i  + 1)
                   pension3_float = round(float(pension3_ini), 0) * (i + 1 - how_int)
                   print("노령연금 :", pension1_float)
                   print("연기연금 :", pension3_float)
                   print("-----------------------")

                   if pension1_float < pension3_float:
                       print("---------------------------")
                       print("연기연금이 노령연금보다 더 클 때")
                       print("노령연금", pension1_float)
                       print("연기연금", pension3_float)
                       z = int(year)-how_int + i
                       print("그 때 나이 : ", z, "세")
                       z = str(z)
                       x = QtWidgets.QTableWidgetItem(z)
                       x.setBackground(QtGui.QColor(255, 0, 0))
                       self.table.setVerticalHeaderItem(i, x)
                       break

               # 그래프 그리기

               age_pension2 = range(int(year), int(year) + 27)  # 조기 연금 나이

               n = list(range(0, int(year) * 2))  # (노령연금) 범위까지 x값은 아무 의미없는 값으로 설정 -> 그래프에 표시하기 위함
               for i in range(int(year)-1, int(year) * 2):
                   n[i] = float(pension0) * (i - int(year)+how_int+1)  # 해당 나이에 받는 연금(누적액)

               m = list(range(0, int(year) * 2))  # (연기연금) 범위까지 x값은 아무 의미없는 값으로 설정 -> 그래프에 표시하기 위함
               for i in range(int(year)-1, int(year) * 2):
                   m[i] = float(pension3_graph) * (i - int(year)+1)

               plt = pg.plot()
               plt.setXRange(age_pension2[0], age_pension2[26])
               plt.setLimits(xMin=age_pension2[0], xMax=age_pension2[26])
               plt.setLimits(yMin=0)
               plt.setGeometry(25, 25, 1000, 500)
               plt.setWindowTitle('조기 및 노령 연금 비교 그래프')
               plt.addLegend()

               c1 = plt.plot(n, pen='g', name='노령 연금')
               c2 = plt.plot(m, pen='y', name='연기 연금')
               c3 = plt.addLine(x=z, pen=(0, 0, 255))


if __name__ == '__main__':
       app = QtWidgets.QApplication(sys.argv)
       app.setStyle(QtWidgets.QStyleFactory.create('Fusion')) # won't work on windows style.
       Frame = MyFrame(None)

       Frame.resize(500,970)
       Frame.show()
       app.exec_()

# 출생연도 입력

# 조기 연금, 연기 연금 선택

# 매달 받는 연금 예상 금액

# 1~5년의 기간 선택

# (조기 연금) 신청 당시 기본 연금액 입력 (A 값에 의해 변화)

# 택1) 조기 연금 - 노령 연금
# (표)를 작성

# 택2) 연기 연금 - 노령 연금
# (표)를 작성

# 결과 - 그래프 (조기),(노령),(연기) 연금 그리기