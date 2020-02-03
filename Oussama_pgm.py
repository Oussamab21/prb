# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testgiu.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from numpy.random import choice
import random



######################################################### THE GUI PART###################################################"



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Bayes prob")
        Dialog.resize(1058, 690)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(800, 90, 251, 521))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(820, 40, 191, 20))
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(630, 610, 99, 27))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(338, 610, 121, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 30, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(470, 30, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(640, 40, 111, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 140, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 210, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 280, 113, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 140, 113, 27))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 210, 113, 27))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(290, 280, 113, 27))
        self.lineEdit_7.setObjectName("lineEdit_7")
        
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 140, 113, 27))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(470, 210, 113, 27))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(470, 280, 113, 27))
        self.lineEdit_11.setObjectName("lineEdit_11")
      
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 280, 67, 17))
        self.label_8.setObjectName("label_8")
        
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 430, 271, 17))
        self.label_10.setObjectName("label_10")
        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(130, 490, 51, 27))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 490, 67, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(220, 490, 67, 17))
        self.label_12.setObjectName("label_12")
        self.lineEdit_18 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(290, 490, 51, 27))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(380, 490, 67, 17))
        self.label_13.setObjectName("label_13")
        self.lineEdit_19 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(470, 490, 51, 27))
        self.lineEdit_19.setObjectName("lineEdit_19")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Bias prob", "Bias prob"))
        self.label.setText(_translate("Dialog", "Liste de boule déja tirée"))
        self.pushButton_1.setText(_translate("Dialog", "Brassage"))
        self.pushButton_2.setText(_translate("Dialog", "Tirer une boule"))
        self.pushButton_2.clicked.connect(recuperer_une_boule)
        self.label_2.setText(_translate("Dialog", " Boules  Rouges"))
        self.label_3.setText(_translate("Dialog", " Boules Blues"))
        self.label_4.setText(_translate("Dialog", "Boules Jaunes "))
        
        self.label_6.setText(_translate("Dialog", "Urne #1"))
        self.label_7.setText(_translate("Dialog", "Urne #2"))
        self.label_8.setText(_translate("Dialog", "Urne#3"))
    
        self.label_10.setText(_translate("Dialog", "Probabilité que la urne ait été choisie"))
        self.label_11.setText(_translate("Dialog", "Urne #1"))
        self.label_12.setText(_translate("Dialog", "Urne #2"))
        self.label_13.setText(_translate("Dialog", "urne #3"))
        
        
        
        
############################################ creating instances of urnes as objects of classes ###############################"        


class urne1:
    # Initializer / Instance Attributes
    def __init__(self):
        self.boules_rouges = 10 
        self.boules_blues = 4
        self.boules_jaunes =2
        self.Pr_R_U1=10/16
        self.Pr_B_U1=4/16
        self.Pr_J_U1=2/16
        self.probabilite1_choisie=0.33
        self.probability_sequence=1
        ui.lineEdit_17.setText(str(self.probabilite1_choisie))
        ui.lineEdit.setText(str(self.boules_rouges))
        ui.lineEdit_5.setText(str(self.boules_blues))
        ui.lineEdit_9.setText(str(self.boules_jaunes))
class urne2:
    def __init__(self):
        self.boules_rouges = 6 
        self.boules_blues = 6
        self.boules_jaunes =0
        self.Pr_R_U2=6/12
        self.Pr_B_U2=6/12
        self.Pr_J_U2=0/12
        self.probabilite2_choisie=0.33
        self.probability_sequence=1
        ui.lineEdit_18.setText(str(self.probabilite2_choisie))
        ui.lineEdit_2.setText(str(self.boules_rouges))
        ui.lineEdit_6.setText(str(self.boules_blues))
        ui.lineEdit_10.setText(str(self.boules_jaunes))

class urne3:
    def __init__(self):
        self.boules_rouges = 4 
        self.boules_blues = 10
        self.boules_jaunes =2
        self.Pr_R_U3=4/16 
        self.Pr_B_U3=10/16
        self.Pr_J_U3=2/16
        self.probabilite3_choisie=0.33
        self.probability_sequence=1        
        ui.lineEdit_19.setText(str(self.probabilite3_choisie))
        ui.lineEdit_3.setText(str(self.boules_rouges))
        ui.lineEdit_7.setText(str(self.boules_blues))
        ui.lineEdit_11.setText(str(self.boules_jaunes))
        
        

############################################################################################################################"



def recuperer_une_boule():

    urn1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    
    urn2=[17,18,19,20,21,22,23,24,25,26,27,28]
    
    urn3=[29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
    
    numberList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
    
    rouge=[1,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,29,30,31,32]
    
    blue=[11,12,13,14,23,24,25,26,27,28,33,34,35,36,37,38,39,40,41,42]
    
    jaune=[15,16,43,44]    
    
    item=random.choice(numberList)
    
    
    
    ####################################################Red case #########################################################""    
    
    
    if item in rouge:
      
       sequencelist.append("rouge")
       
     
       
       
       ur1.probability_sequence=ur1.probability_sequence*ur1.Pr_R_U1
       ur2.probability_sequence=ur2.probability_sequence*ur2.Pr_R_U2
       ur3.probability_sequence=ur3.probability_sequence*ur3.Pr_R_U3
       
      
       Proba2_urne1_rouge=ur1.probabilite1_choisie*ur1.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
       
       ui.lineEdit_17.setText(str("%.2f"%Proba2_urne1_rouge))
       
       
          
       Proba2_urne2_rouge=ur2.probabilite2_choisie*ur2.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
       ui.lineEdit_18.setText(str("%.2f"%Proba2_urne2_rouge))
       
      
       
       
              
       Proba2_urne3_rouge=ur3.probabilite3_choisie*ur3.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
       
       
       ui.lineEdit_19.setText(str("%.2f"%Proba2_urne3_rouge)) 
       ui.textEdit.append("Rouge")        
       
       
    ############################################ Blue case ##########################################################"       
       
       
    if item in blue:  
       
       sequencelist.append("blue")
     
       
       ur1.probability_sequence=ur1.probability_sequence*ur1.Pr_B_U1
       ur2.probability_sequence=ur2.probability_sequence*ur2.Pr_B_U2
       ur3.probability_sequence=ur3.probability_sequence*ur3.Pr_B_U3 
       
       
       
       
       
       
       Proba2_urne1_blue=ur1.probabilite1_choisie*ur1.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
             
       ui.lineEdit_17.setText(str("%.2f"%Proba2_urne1_blue))
       
       Proba2_urne2_blue=ur2.probabilite2_choisie*ur2.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
             
       ui.lineEdit_18.setText(str("%.2f"%Proba2_urne2_blue))
       
       Proba2_urne3_blue=ur3.probabilite3_choisie*ur3.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
       
       ui.lineEdit_19.setText(str("%.2f"%Proba2_urne3_blue))
       ui.textEdit.append("Blue")
       
    #################################################### Yellow case ######################################################""       
       
       
    if item in jaune:    
       
       sequencelist.append("jaune")
       
       
       ur1.probability_sequence=ur1.probability_sequence*ur1.Pr_J_U1
       ur2.probability_sequence=ur2.probability_sequence*ur2.Pr_J_U2
       ur3.probability_sequence=ur3.probability_sequence*ur3.Pr_J_U3        
       
       Proba2_urne1_jaune=ur1.probabilite1_choisie*ur1.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
       
       ui.lineEdit_17.setText(str("%.2f"%Proba2_urne1_jaune))
       
       Proba2_urne2_jaune=ur2.probabilite2_choisie*ur2.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
       
       ui.lineEdit_18.setText(str("%.2f"%Proba2_urne2_jaune))
       
       Proba2_urne3_jaune=ur3.probabilite3_choisie*ur3.probability_sequence/(ur1.probabilite1_choisie*ur1.probability_sequence+ur2.probabilite2_choisie*ur2.probability_sequence+ur3.probabilite3_choisie*ur3.probability_sequence)
      
       ui.lineEdit_19.setText(str("%.2f"%Proba2_urne3_jaune))
       
       ui.textEdit.append("Jaune")
       
################################################################  MAIN ############################################# 

#def 
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    Dialog = QtWidgets.QDialog()
    
    ui = Ui_Dialog()
    
    ui.setupUi(Dialog)
    
    ur1=urne1()
    ur2=urne2()
    ur3=urne3()
    sequencelist=[]
    
    Dialog.show()
    
    sys.exit(app.exec_())
