import socket
from Crypto.Cipher import DES

def client():

    host_name = socket.gethostname()
    IPAddress = socket.gethostbyname(host_name)
    print("Your Computer Name is:" + host_name)
    print("Your Computer IP Address is:" + IPAddress)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IPAddress, 1100))
    data = s.send(b'hola')
    s.close()


if __name__ == '__main__':
    client()