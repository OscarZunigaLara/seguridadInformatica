from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes

from time import time

def server():

    import socket
    host_name = socket.gethostname()
    IPAddress = socket.gethostbyname(host_name)
    print("Your Computer Name is:" + host_name)
    print("Your Computer IP Address is:" + IPAddress)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.bind((IPAddress, 1100))
    s.listen(1)
    connection, address = s.accept();
    with connection:

        a = connection.recv(1024)
        key = connection.recv(1024)
        nonce = connection.recv(1024)
        tag =connection.recv(1024)

        print(a)
        print(key)
        print(nonce)
        print(tag)
        start = time()

        cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(a)
        try:
            cipher.verify(tag)
            print("THIS MESSAGE IS AUTHENTIC : ", plaintext)

        except ValueError:
            print("KEY INCORRECT OR MESSAGE CORRUPTED")

        connection.close();
        print(f'Time taken to run: {time() - start} seconds')

if __name__ == '__main__':
    server()