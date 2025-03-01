from usocket import socket
from machine import Pin, SPI
import network
import time
import socket
import uos
import gc
import sdcard
from time import localtime

# 初始化SD卡
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
uos.mount(sd, "/sd")  # 挂载SD卡
print(uos.listdir('/sd'))  # 列出SD卡中的文件

# 初始化网络
spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
nic = network.WIZNET5K(spi, Pin(17), Pin(20))
nic.active(True)
nic.ifconfig(('192.168.137.100', '255.255.255.0', '192.168.137.1', '8.8.8.8'))
print('IP address:', nic.ifconfig())
while not nic.isconnected():
    time.sleep(1)

# 初始化W5x00芯片
def w5x00_init():
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    nic = network.WIZNET5K(spi, Pin(17), Pin(20))
    nic.active(True)
    nic.ifconfig(('192.168.137.100', '255.255.255.0', '192.168.137.1', '8.8.8.8'))
    print('IP address:', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)
    return nic

month_name = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 发送目录列表数据
def send_list_data(path, dataclient, full):
    try:
        for fname in uos.listdir(path):
            dataclient.sendall(make_description(path, fname, full))
    except:
        pattern = path.split("/")[-1]
        path = path[:-(len(pattern) + 1)]
        if path == "":
            path = "/"
        for fname in uos.listdir(path):
            if fncmp(fname, pattern):
                dataclient.sendall(make_description(path, fname, full))

# 生成文件描述
def make_description(path, fname, full):
    # 实现文件描述的生成
    # ...

# 发送文件数据
def send_file_data(path, dataclient):
    # 发送文件数据
    # ...

# 保存文件数据
def save_file_data(path, dataclient, mode):
    # 保存文件数据
    # ...

# 获取绝对路径
def get_absolute_path(cwd, payload):
    # 获取绝对路径
    # ...

# 比较文件名和模式
def fncmp(fname, pattern):
    # 比较文件名和模式
    # ...

# FTP服务器函数
def ftpserver():
    DATA_PORT = 13333
    ftpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    datasocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 设置套接字选项
    ftpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    datasocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 绑定FTP套接字和数据套接字
    ftpsocket.bind(socket.getaddrinfo("0.0.0.0", 21)[0][4])
    datasocket.bind(socket.getaddrinfo("0.0.0.0", DATA_PORT)[0][4])
    
    ftpsocket.listen(1)
    datasocket.listen(1)
    datasocket.settimeout(10)
    
    msg_250_OK = '250 OK\r\n'
    msg_550_fail = '550 Failed\r\n'
    
    try:
        dataclient = None
        fromname = None
        
        while True:
            cl, remote_addr = ftpsocket.accept()
            cl.settimeout(300)
            cwd = '/'
            
            try:
                cl.sendall("220 Hello, this is the RP2020.\r\n")
                
                while True:
                    gc.collect()
                    data = cl.readline().decode("utf-8").rstrip("\r\n")
                    
                    if len(data) <= 0:
                        print("Client disappeared")
                        break
                        
                    command = data.split(" ")[0].upper()
                    payload = data[len(command):].lstrip()
                    path = get_absolute_path(cwd, payload)
                    
                    # 处理FTP命令
                    # ...
                    
            except Exception as err:
                print(err)
                
            finally:
                cl.close()
                cl = None
                
    finally:
        datasocket.close()
        ftpsocket.close()
        
        if dataclient is not None:
            dataclient.close()

# 主函数
def main():
    ftpserver()

if __name__ == "__main__":
    main()
