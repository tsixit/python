
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLineEdit
import socket
import chatwidget
# from PyQt5.uic import loadUi : permet d'importer le fichier UI directement sans faire la conversion en python

# from PyQt5.uic import loadUi # on peut aussi importer directement le fichier ui de Qt

# PyCharm : Alt+Entrée = Importer l'entité sur lequel est le curseur


class Server(QThread):

    message_recu = pyqtSignal(str, str)

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.bind(('', 12345))
        s.listen()
        while True:
            print("En attente d'une connexion...")
            client, address = s.accept()
            print("Connexion acceptée !")
            print(client)
            print(address)

            octets = client.recv(1024)
            print(octets)
            message = octets.decode('utf-8')
            print(message)
            # self.messages.append("Un message est arrivé !")
            self.message_recu.emit(message, address[0])

            client.close()

        s.close()


class ChatDialog(QWidget, chatwidget.Ui_ChatDialog):

    def __init__(self):
        super().__init__(flags=Qt.Widget)

        # self.ui = chatwidget.Ui_ChatDialog()
        # self.ui.setupUi(self)
        # self.ui._quitter.clicked.connect(self._quit)

        # loadUi('chat_dialog.ui', self) : charge le UI

        self.setupUi(self)
        self._hote.setText('localhost')
        self._port.setText('12345')
        self._message.returnPressed.connect(self._send)

        server = Server()
        server.start()
        # server.messages = messages
        server.message_recu.connect(self._ajouter_message)
        self._server = server

    def __old_setup_ui(self):
        self.setGeometry(2000, 100, 600, 300)
        # x = 2000, y = 100, largeur = 600, hauteur = 300

        quitter = QPushButton('Quitter', self)
        quitter.clicked.connect(self._quit)
        self._quitter = quitter

        messages = QTextEdit(self)
        messages.setGeometry(10, 40, 580, 150)
        messages.setPlaceholderText("Messages...")
        messages.setReadOnly(True)
        self._messages = messages

        messages.append("Ligne 1")
        messages.append("Ligne 2")
        messages.append("Ligne 3")

        hote = QLineEdit(self)
        hote.setGeometry(10, 210, 400, 25)
        hote.setPlaceholderText("Hôte de destination...")
        hote.setText('localhost')
        self._hote = hote

        print(hote.text())

        port = QLineEdit(self)
        port.setGeometry(420, 210, 170, 25)
        port.setPlaceholderText("Port...")
        port.setText('12345')
        port.setValidator(QIntValidator())
        self._port = port

        print(port.text())

        message = QLineEdit(self)
        message.setGeometry(10, 260, 400, 25)
        message.setPlaceholderText("Votre message...")
        message.returnPressed.connect(self._send)
        message.setFocus()
        self._message = message

        envoyer = QPushButton('Envoyer', self)
        envoyer.setGeometry(420, 260, 170, 25)
        envoyer.clicked.connect(self._send)
        self._envoyer = envoyer

        server = Server()
        server.start()
        # server.messages = messages
        server.message_recu.connect(self._ajouter_message)
        self._server = server

    def _quit(self):
        application = QApplication.instance()
        application.quit()

    def _send(self):
        print("Vous avez cliqué sur le bouton Envoyer !")

        h = self._hote.text()
        p = int(self._port.text())
        m = self._message.text()
        print(h, p, m)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((h, p))
        s.send(m.encode('utf-8'))
        s.close()

        self._messages.append("{} <= {}".format(h, m))
        self._message.setText('')

    def _ajouter_message(self, message, ip):
        # print("Un message est arrivé !")
        # self._messages.append("Un message est arrivé !")
        self._messages.append("{} => {}".format(ip, message))


if __name__ == '__main__':

    app = QApplication([])

    # fenetre = QWidget(flags=Qt.Widget)
    # bouton = QPushButton('Bouton', fenetre)
    # fenetre.show()

    dialog = ChatDialog()
    dialog.show()

    app.exec_()
