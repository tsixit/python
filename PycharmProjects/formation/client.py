import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.connect(('localhost', 12345))
s.connect(('192.168.75.56', 12345))

import socket

# Luc : 192.168.75.56
# Charles : 192.168.75.131
# François : 192.168.75.165
# Paul : 192.168.75.110
# Roman : 192.168.75.163
# Alexis : 192.168.75.119


def envoyer_message(ip, port, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    # message = "Message en provenance de Luc..."
    s.send(message.encode('utf-8'))
    s.close()


envoyer_message('192.168.75.131', 12345, "Message en provenance de Luc...")
envoyer_message('192.168.75.165', 12345, "Message en provenance de Luc...")
envoyer_message('192.168.75.110', 12345, "Message en provenance de Luc...")
envoyer_message('192.168.75.163', 12345, "Message en provenance de Luc...")
envoyer_message('192.168.75.119', 12345, "Message en provenance de Luc...")
