import socket
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from time import time


def client():
    start = time()

    host_name = socket.gethostname()
    IPAddress = socket.gethostbyname(host_name)
    print("Your Computer Name is:" + host_name)
    print("Your Computer IP Address is:" + IPAddress)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IPAddress, 1100))

    data = (b'MENSAJE ENCRIPTADO CON DES')
    key = get_random_bytes(8)

    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    #print(ciphertext)
    #print(nonce)
    #print(tag)

    data = s.send(ciphertext)
    keysend = s.send(key)
    nonceSend = s.send(nonce)
    tagSende = s.send(tag)

    s.close()


    print(f'Time taken to run: {time() - start} seconds')

if __name__ == '__main__':
    client()