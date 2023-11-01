import serial

ser = serial.Serial('COM1', baudrate=9600, timeout=1) # Change the Comm Port #
ser.write(b'username\n') # If there is a console username and pass, enter here
ser.write(b'password\n')

response = ser.read(1024)
print(response.decode('utf-8'))

ser.close()


