import socket


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET = socket réseau (port)
# socket.SOCK_STREAM = TCP

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # réutiliser le port, sans attendre qu'il soit libéré

s.bind(('', 12345))#  '' on n'accepte tout le monde
# 'localhost' = accepter uniquement les connexions locales
# '' = accepter les connexion de n'importe où
# 12345 = port

# Luc : 192.168.75.56
# Charles : 192.168.75.131
# François : 192.168.75.165
# Paul : 192.168.75.110
# Roman : 192.168.75.163
# Alexis : 192.168.75.56

s.listen()

while True:
    print("En attente d'une connexion...")
    client, address = s.accept() # accepte seulement une seule connexion
    print("Connexion acceptée !")
    print(client)
    print(address)

    octets = client.recv(1024)
    print(octets)
    message = octets.decode('utf-8')
    print(message)

    client.close()

s.close()


