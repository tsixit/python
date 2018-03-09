# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatDialog(object):
    def setupUi(self, ChatDialog):
        ChatDialog.setObjectName("ChatDialog")
        ChatDialog.resize(687, 639)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChatDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._quitter = QtWidgets.QPushButton(ChatDialog)
        self._quitter.setObjectName("_quitter")
        self.horizontalLayout.addWidget(self._quitter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._messages = QtWidgets.QTextEdit(ChatDialog)
        self._messages.setObjectName("_messages")
        self.verticalLayout.addWidget(self._messages)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self._hote = QtWidgets.QLineEdit(ChatDialog)
        self._hote.setText("")
        self._hote.setObjectName("_hote")
        self.horizontalLayout_10.addWidget(self._hote)
        self._port = QtWidgets.QLineEdit(ChatDialog)
        self._port.setMaximumSize(QtCore.QSize(85, 16777215))
        self._port.setObjectName("_port")
        self.horizontalLayout_10.addWidget(self._port)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self._message = QtWidgets.QLineEdit(ChatDialog)
        self._message.setObjectName("_message")
        self.horizontalLayout_11.addWidget(self._message)
        self._envoyer = QtWidgets.QPushButton(ChatDialog)
        self._envoyer.setMaximumSize(QtCore.QSize(85, 16777215))
        self._envoyer.setObjectName("_envoyer")
        self.horizontalLayout_11.addWidget(self._envoyer)
        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi(ChatDialog)
        self._quitter.clicked.connect(ChatDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ChatDialog)

    def retranslateUi(self, ChatDialog):
        _translate = QtCore.QCoreApplication.translate
        ChatDialog.setWindowTitle(_translate("ChatDialog", "Form"))
        self._quitter.setText(_translate("ChatDialog", "Quitter"))
        self._hote.setPlaceholderText(_translate("ChatDialog", "Hôte..."))
        self._port.setPlaceholderText(_translate("ChatDialog", "Port..."))
        self._message.setPlaceholderText(_translate("ChatDialog", "Votre message..."))
        self._envoyer.setText(_translate("ChatDialog", "Envoyer"))

