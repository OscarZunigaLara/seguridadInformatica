import socket
from Crypto.Cipher import DES
from Crypto.Cipher import AES

def client():

    host_name = socket.gethostname()
    IPAddress = socket.gethostbyname(host_name)
    print("Your Computer Name is:" + host_name)
    print("Your Computer IP Address is:" + IPAddress)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IPAddress, 1100))

    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    msg = cipher.iv + cipher.encrypt("hola, mensaje encriptado en DES")
    print(msg)
    data = s.send(msg)
    #data = s.send(b'hola')
    s.close()


if __name__ == '__main__':
    client()