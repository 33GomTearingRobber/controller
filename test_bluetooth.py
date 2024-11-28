from machine import Pin,UART # Pin, UART 모듈 가져오기
import utime # time 모듈 가져오기

#UART 전송 속도 (HC-05 = 9600)
uart = UART(0,9600)

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
