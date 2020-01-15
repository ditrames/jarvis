import serial
class seriallib:
    def __init__(self, baudrate, code):
        self.connection = None
        pass
    def connect(self):
        for i in "COM0", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8":
            try:
                ser = serial.Serial(i, baudrate,)
                time.sleep(7)
                print("connected at", i)
                ser.write(code.encode())
                data = ser.readline()
                if data == code:
                    self.connection = ser
                    return 1
            except Exception as e:
                print(e)
        return 0
    
    def send(self, data):
        self.connection.write(data.encode())
    def recv():
        return self.connection.readlines()

        