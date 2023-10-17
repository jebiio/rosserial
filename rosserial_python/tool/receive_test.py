# struct.pack 참고 : https://docs.python.org/ko/3/library/struct.html
# rosserial -> PC usb serial
import sys
import serial
import struct

class IcdToMC:
    def __init__(self):
        self.timestamp =0
        self.t_sec=0           
        self.delt_sec=0.0

        self.delx_rps=0.0
        self.dely_rps=0.0
        self.qual=0.0

        self.gx_rps=0.0
        self.gy_rps=0.0
        self.gz_rps=0.0

        self.ax_mps2=0.0
        self.ay_mps2=0.0
        self.az_mps2=0.0

        self.h_mtr=0.0

        self.mx_gauss=0.0
        self.my_gauss=0.0
        self.mz_gauss=0.0

        self.rsv0=0.0
        self.rsv1=0.0
        self.rsv2=0.0
        self.rsv3=0.0

    def toBuffer(self):
        return struct.pack('<Qdffffffffffffffffff', self.timestamp, self.t_sec, self.delt_sec, self.delx_rps, self.dely_rps, self.qual, self.gx_rps, self.gy_rps, self.gz_rps, self.ax_mps2, self.ay_mps2, self.az_mps2, self.h_mtr, self.mx_gauss, self.my_gauss, self.mz_gauss, self.rsv0, self.rsv1, self.rsv2, self.rsv3)

    def updateValue(self):
        pass

def main():
    ser = serial.Serial()

    ser.port = '/dev/ttyUSB1' # 변경하시오
    ser.baudrate = 115200 
    ser.open()

    while(True):
        in_bytes = ser.read(63)
        print('\nreceived : ', in_bytes)
        # in_struct = struct.unpack('<Qdffffffffffffffffff', in_bytes)
        # print(in_struct)
    ser.close()

if __name__=="__main__":
    main()