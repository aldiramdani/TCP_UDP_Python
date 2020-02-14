import socket

UDP_IP = '192.168.1.6'
UDP_PORT = 5005
PESAN = 'Halo Kelompok Kami Beranggota kan 1. Aldi Ramdani , 2. Rivkal Sanjaya, 3. Aulia Ikvanda Yoren'

print('Target IP : ',UDP_IP)
print('Target Port : ',UDP_PORT)
print('Pesan : ',PESAN)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for x in range(10):
    sock.sendto(PESAN.encode(),(UDP_IP,UDP_PORT))