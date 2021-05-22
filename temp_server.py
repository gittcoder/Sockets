import socket
HOST='127.0.0.1'
PORT=5760
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("Socket initialized")
    conn,addr=s.accept()
    count=0
    with conn:
        print(f'Connected with {addr}')
        while True:
            data=conn.recv(1024).decode('utf-8')
            print(data)
            if not data:
                break
            else :
                print(f'Sending acknowledgement for {count}')
                conn.sendall('Acknowledgement for data sent '.encode('utf-8'))
                count+=1