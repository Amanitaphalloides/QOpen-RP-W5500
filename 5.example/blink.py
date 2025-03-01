import machine
import time

#设置引脚
led_pin = machine.Pin(25, machine.Pin.OUT)

while True:
    led_pin.value(1)   # 点亮LED
    time.sleep(0.5)    # 等待0.5秒
    led_pin.value(0)   # 熄灭LED
    time.sleep(0.5)    # 等待0.5秒
