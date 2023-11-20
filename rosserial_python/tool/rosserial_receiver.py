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
                data = self.serial_port.read(34)
                if data:
                    print(data)
            time.sleep(0.01)


class SerialWriter(threading.Thread):

    def __init__(self, serial_port, lock):
        super().__init__()
        self.serial_port = serial_port
        self.lock = lock

    def run(self):
        while True:
            with self.lock:
                packet = bytearray(63)
                print('write!!!')
                self.serial_port.write(packet)
            time.sleep(0.5)    # time.sleep(0.01)


if __name__ == "__main__":
    serial_port = serial.Serial("/dev/ttyUSB0", 57600, timeout=1)
    lock = Lock()

    reader = SerialReader(serial_port, lock)
    writer = SerialWriter(serial_port, lock)

    reader.start()
    writer.start()

    reader.join()
    writer.join()