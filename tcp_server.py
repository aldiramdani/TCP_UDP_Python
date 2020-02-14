import socket 
TCP_IP = '192.168.1.6'
TCP_PORT = 8080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)

while 1:
    conn,addr = s.accept()
    print('Alamat : ', addr)
    data = conn.recv(BUFFER_SIZE)
    print('Pesan Diterima : ',data.decode())
    conn.send(data)
conn.close()