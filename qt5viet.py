#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/usr/bin/python2


import unicodedata, sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.courant=' '
        self.combo_choix={}
        self.combo_choix['-- NOOP --'] = None
        self.combo_choix.update({ unicodedata.name(c) : c for c in 
            "\u0300\u0301\u0303\u0306\u0309\u0323\u031b\u0111" })
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Création de la liste déroulante
        self.comboBox = QComboBox()
        for libelle in self.combo_choix.keys() :
            self.comboBox.addItem(libelle)

        # Connecter la fonction de traitement à l'événement de changement de sélection
        self.comboBox.currentIndexChanged.connect(self.selectionChanged)

        layout.addWidget(self.comboBox)
        self.textEdit = QLineEdit()
        self.textEdit.setPlaceholderText("saisissez du texte");
        # self.textEdit.textChanged.connect(self.textChanged)
        layout.addWidget(self.textEdit)
        self.textCompo = QLineEdit()
        layout.addWidget(self.textCompo)
        self.bouton = QPushButton("convertir")
        self.bouton.clicked.connect(self.convertir)
        layout.addWidget(self.bouton)
        self.setLayout(layout)

    def convertir(self):
        txt1 = self.textEdit.text()
        txt2=unicodedata.normalize('NFC', txt1)
        if txt1 == txt2 :
            print("aucun changement")
        print(unicodedata.name(txt2[-1]))
        self.textCompo.setText(txt2)

    def selectionChanged(self, index):
        # Récupérer la sélection actuelle
        cle = self.comboBox.currentText()
        val = self.combo_choix[cle]
        self.courant = val
        if not val :
            return
        texte_courant = self.textEdit.text()
        self.textEdit.setText(texte_courant + val)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('Liste déroulante PyQt5')
    window.show()
    sys.exit(app.exec_())

