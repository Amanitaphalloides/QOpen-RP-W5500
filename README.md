# **QOpen-RP-W5500**
QOpen-RP-W5500 is an open source DEV_Board with RP2040 & WIZnet® W5500. Communication between RP2040 and W5500 is conducted using the SPI bus.

# **Development guide☸**
## MicroPython
1. Download firmware
2. Connect board to PC with a Type-C wire
3. Develop in Python environment 

## Arduino
1. Connect board to PC with a Type-C wire
2. Develop in Arduino environment

# **Tutorial link🔗**
[bbs.eeworld.com.cn](bbs.eeworld.com.cn/thread-1272177-1-1.html)

# **HW Prj🏠**
[oshwhub.com/quax](oshwhub.com/quax/qopenrp-w5500-ethernet-developme)

# **Physical image**
![IMG_1.jpg](https://image.lceda.cn/oshwhub/pullImage/a3f13efaf03f4c70962d6f293f52771d.jpg)

![IMG_3.jpg](https://image.lceda.cn/oshwhub/pullImage/020fac0a696d40de8bf5195c3a38595b.jpg)

**There are some discrepancies with the released version.**
**All can be used normally**

# **Actual effect🔨**

## PING
![PING](https://image.lceda.cn/oshwhub/pullImage/282738e05831440c979c02cde07487ee.png)


## NTP example
![NTP](https://image.lceda.cn/oshwhub/pullImage/997ed86eca534435839af0bd478e1019.png)

# **Precautions❗**
1. W5500's working current is high. Please be sure to attach the heat sink.
2. Make sure that the LDO outputs 3.3V normally before soldering other components.

# **FAQ❓**
## Why my PC can’t recognize the board？
Please check whether the RP2040 pins are cold soldered.

## Why my PWR LED does not light up？
Please check whether the fuse is burned out or the board has a soldering problem.

## 
