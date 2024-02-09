import socket
from ev3dev.auto import * 

mL = LargeMotor('outA'); mL.stop_action = 'hold'
mB = LargeMotor('outB'); mL.stop_action = 'hold'

HOST = "192.168.32.18"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by addr")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received data!r")
            if data == b'q':
                break
            elif data == b'a':
                print("Received a")
                mL.run_forever(speed_sp=250)
            elif data == b'A':
                print("Received A")
                mL.stop()
            elif data == b'b':
                print("Received b")
                mB.run_forever(speed_sp=250)
            elif data == b'B':
                print("Received B")
                mB.stop()