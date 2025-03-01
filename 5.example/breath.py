import machine
import time

#设置引脚
led_pin = machine.Pin(25, machine.Pin.OUT)

def breathe_led():
    pwm = machine.PWM(led_pin)
    while True:
        for duty_cycle in range(0, 5000, 100):
            pwm.duty_u16(duty_cycle)
            time.sleep_ms(10)
        for duty_cycle in range(5000, 0, -100):
            pwm.duty_u16(duty_cycle)
            time.sleep_ms(10)

breathe_led()
