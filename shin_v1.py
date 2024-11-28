import serial

ser = serial.Serial("/dev/serial0", baudrate=9600)
try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)
finally:
    ser.close()
