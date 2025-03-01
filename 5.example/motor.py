import machine
import utime

# 设置8号脚为输出引脚，设置高电平
pin8 = machine.Pin(8, machine.Pin.OUT)
pin8.value(1)

# 设置9号脚为输出引脚，设置低电平
pin9 = machine.Pin(9, machine.Pin.OUT)
pin9.value(0)

# 设置7号脚为PWM输出
pwm = machine.PWM(machine.Pin(7))

while True:
    pwm.freq(1000)       #设置PWM频率为1kHz
    pwm.duty_u16(32768)  #50%占空比对应的duty cycle值为32768

    utime.sleep(5)
    
    pwm.freq(500)        #设置PWM频率为500Hz
    pwm.duty_u16(16384)  #25%占空比
    
    utime.sleep(5)