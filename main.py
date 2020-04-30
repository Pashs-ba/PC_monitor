import psutil
import serial
import time


class PCMonitor:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB' + self.find_open_port(), 9600)  # find open serial port

    @staticmethod
    def find_open_port():
        ports = ['0', '1', '2', '3']
        while True:  # need to run program in tree while devise off
            for port in ports:
                try:
                    serial.Serial('/dev/ttyUSB' + port, 9600)
                    return port
                except:
                    pass


if __name__ == '__main__':
    pass
