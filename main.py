import psutil
import serial
import datetime
import time


def find_open_port():
    """Find open serial port"""
    ports = ['0', '1', '2', '3']
    while True:  # need to run program in tree while all port close
        for port in ports:
            try:
                serial.Serial('/dev/ttyUSB' + port, 9600)
                return port
            except:
                pass


def main():
    while True:
        ser = serial.Serial('/dev/ttyUSB' + find_open_port(), 9600)
        try:  # if devise is off
            while True:
                proc = max(psutil.cpu_percent(interval=1, percpu=True))  # get most loaded core
                ram = psutil.virtual_memory().used/psutil.virtual_memory().total*100  # percents of ram using
                now = datetime.datetime.now()  # now time
                ser.write(str(str(int(proc)) + ' ').encode())  # need to refactor
                ser.write(str(str(int(ram)) + ' ').encode())
                ser.write(str(str(int(now.hour)) + ' ').encode())
                ser.write(str(int(now.minute)).encode())
                time.sleep(1)
        except:
            pass


if __name__ == '__main__':
    main()
