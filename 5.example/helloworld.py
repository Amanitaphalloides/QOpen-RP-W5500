from machine import Pin,SPI,UART
import time

# UART0初始化
uart = UART(0, baudrate=115200, bits=8, stop=1)

while True:
    # 打印"Hello World"到串口
    uart.write("Hello World\r\n")

    # 等待
    time.sleep(1)