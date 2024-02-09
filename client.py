import socket
HOST = "192.168.32.18"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        char = input("Enter a character: ")
        s.sendall(bytes(char, "utf-8"))
    data = s.recv(1024)

print(f"Received {data!r}")