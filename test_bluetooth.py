import bluetooth

# Bluetooth 서버 소켓 설정
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))  # 아무 포트에서 대기
server_socket.listen(1)

# 연결을 기다림
print("Waiting for Bluetooth connection...")
client_socket, client_info = server_socket.accept()
print("Accepted connection from ", client_info)

# 데이터 처리 루프
try:
    while True:
        # 데이터 수신
        data = client_socket.recv(1024).decode('utf-8')  # 데이터를 받아서 문자열로 디코딩
        print("Received data: ", data)

        # 수신된 데이터에 따른 동작
        if 'w' in data:
            print("Moving Forward")
        elif 's' in data:
            print("Moving Backward")
        elif 'a' in data:
            print("Turning Left")
        elif 'd' in data:
            print("Turning Right")
        else:
            print("Invalid Command")
        
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client_socket.close()
    server_socket.close()
