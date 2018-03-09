from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, \
    QLineEdit  # Pour faire une interface graphique
import socket

# PyCharm : Alt+Entrée = Importer l'entité sur lequel est le curseur

class ChatDialog(QWidget): # Cette class hérite de la classe QWidget

    def __init__(self):
        super().__init__(flags=Qt.Widget)# ici ce n'est pas une héritage

        self.setGeometry(2000, 100, 600, 300)
        # x = 100, y = 100, largeur = 600, hauteur = 300
        quitter = QPushButton('Quitter', self)
        quitter.clicked.connect(self._quit)# _quit on ne veut pas qu'il soit exécuté à l'exterieur de cette classe
        self._quitter = quitter

        messages = QTextEdit(self) # crée un champ de text
        messages.setGeometry(10, 40, 500, 150)
        messages.setPlaceholderText("Messages...")
        self._messages = messages


        hote = QLineEdit(self)
        hote.setGeometry(10, 210, 400, 25)
        hote.setPlaceholderText("Hôe de destination...")
        hote.setText('localhost')
        self._hote = hote # on récupère le composant champ text


        print(hote.text()) # recupère le text qui est dedans

        port = QLineEdit(self)
        port.setGeometry(420, 210, 170, 25)
        port.setPlaceholderText("Port...")
        port.setText('12345')
        self._port = port

        print(port.text())

        message = QLineEdit(self) # message qu'on va envoyer
        message.setGeometry(10, 260, 400, 25)
        message.setPlaceholderText("Votre message...")
        self._message = message

        envoyer = QPushButton('Envoyer', self)
        envoyer.setGeometry(420, 260, 170, 25)
        envoyer.clicked.connect(self._send)
        self._envoyer = envoyer


    def _quit(self):
        application = QApplication.instance()
        application.quit() # Arrête l'application

    def _send(self):
        # print(self._message.text())
        # print(self._hote.text())
        # print(self._port.text())
        m = (self._message.text())
        h = (self._hote.text())
        p = int((self._port.text()))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((h, p))
        s.send(m.encode("utf-8"))
        s.close()

if __name__ == '__main__':
    app = QApplication([]) # Instancie l'application

    # fenetre = QWidget(flags = Qt.Widget)
    # bouton = QPushButton('Bouton', fenetre)
    # fenetre.show()
    # c'est pas vraiment comme ça qu'on crée une fenetre, on crée plutôt une classe

    dialog = ChatDialog()
    dialog.show()
    app.exec_() # lance l'application