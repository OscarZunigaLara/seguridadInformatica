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
        a = connection.recv(1024);
        print(a.decode("ascii"))
        connection.close();


if __name__ == '__main__':
    server()