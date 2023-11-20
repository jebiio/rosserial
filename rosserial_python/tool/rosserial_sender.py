import serial
import threading
from threading import Lock
import time

class SerialReader(threading.Thread):

    def __init__(self, serial_port, lock):
        super().__init__()
        self.serial_port = serial_port
        self.lock = lock

    def run(self):
        while True:
            with self.lock:
                print('read!!!')
                data = self.serial_port.read(63)
                if data:
                    print(data)
            time.sleep(0.01)


class SerialWriter(threading.Thread):

    def __init__(self, serial_port, lock):
        super().__init__()
        self.serial_port = serial_port
        self.lock = lock
        self.count = 0

    def run(self):
        while True:
            with self.lock:
                print('write!!!')
                packet = bytearray(34)
                packet[0] = 0xAA
                packet[33] = self.count % 255
                self.serial_port.write(packet)
                self.count = self.count + 1
            time.sleep(0.2)
                # time.sleep(0.5)


if __name__ == "__main__":
    serial_port = serial.Serial("/dev/ttyUSB1", 57600, timeout=1)
    lock = Lock()

    reader = SerialReader(serial_port, lock)
    writer = SerialWriter(serial_port, lock)

    reader.start()
    writer.start()

    reader.join()
    writer.join()