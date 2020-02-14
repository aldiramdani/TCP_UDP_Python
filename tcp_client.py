import socket 
TCP_IP = '192.168.1.6'
TCP_PORT = 8080
BUFFER_SIZE = 1024
PESAN = 'Halo Kelompok Kami Beranggota kan 1. Aldi Ramdani , 2. Rivkal Sanjaya, 3. Aulia Ikvanda Yoren'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(PESAN.encode())
data = s.recv(BUFFER_SIZE)
s.close

print('Pesan Diterima : ',data.decode())