from usocket import socket
from machine import Pin, SPI, UART, RTC
import network
import time
import ntptime

uart = machine.UART(0, baudrate=9600)

#W5x00芯片初始化
def w5x00_init():
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    nic = network.WIZNET5K(spi, Pin(17), Pin(20))  # 使用SPI总线，设置CS和RESET引脚
    nic.active(True)
    
    #手动设置IP地址，子网掩码，网关和DNS服务器地址
    nic.ifconfig(('192.168.137.144', '255.255.255.0', '192.168.137.1', '8.8.8.8'))
    
    print('IP address:', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
        #print(nic.regs())  # 可以打印芯片的寄存器状态进行调试

def show_local_time(timezone=8):
    rtc = RTC()
    now = time.time()
    now += timezone * 3600
    t = time.localtime(now)
    print(f'{t[0]} - {t[1]:02d}-{t[2]:02d} {t[3]:02d}:{t[4]:02d}:{t[5]:02d}')
    uart.write(f'{t[0]} - {t[1]:02d}-{t[2]:02d} {t[3]:02d}:{t[4]:02d}:{t[5]:02d}\n')

def main():
    w5x00_init()
    
    #手动设置一个错误的系统时间
    rtc = RTC()
    rtc.datetime((2021,1,1,1,1,1,1,1))  # 年、月、日、星期、时、分、秒、亚秒
    print('校时前系统时间：')
    show_local_time()
    
    #使用NTP服务器校准时间
    print('开始NTP校时...')
    ntptime.host = 'ntp1.aliyun.com'
    ntptime.settime()
    print('校时后系统时间：')
    show_local_time()
    while True:
        show_local_time()
        time.sleep(1)

if __name__ == "__main__":
    main()
