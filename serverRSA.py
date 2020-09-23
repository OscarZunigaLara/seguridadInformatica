
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
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
        start = time()

        print(a)
        private_key = RSA.import_key(open("private.pem").read())
        file_in = open("encrypted_data.bin", "rb")
        enc_session_key, nonce, tag, ciphertext = \
            [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        print(data.decode("utf-8"))
        connection.close();
        print(f'Time taken to run: {time() - start} seconds')

if __name__ == '__main__':
    server()