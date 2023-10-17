# rosserial

[![Build Status](https://travis-ci.org/ros-drivers/rosserial.svg?branch=melodic-devel)](https://travis-ci.org/ros-drivers/rosserial)

Please see [rosserial on the ROS wiki](http://wiki.ros.org/rosserial) to get started.

## 실행
```bash
rosrun rosserial_python serial_node.py _port:=/dev/ttyUSB0 _baud:=115200
```

## test
* 준비
  * serial usb 장치 연결
    * 장치 1
      * 33 bytes sender로 실행
    * 장치 2
      * rosserial_python으로 읽기
```bash
python3 ./rosserial_python/tool/sender.py
```
