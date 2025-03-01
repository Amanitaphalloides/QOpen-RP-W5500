from usocket import socket
from machine import Pin, SPI, UART
import network
import time

uart = UART(0, baudrate=115200, bits=8, stop=1)

# W5x00 chip initialization
def w5x00_init():
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    nic = network.WIZNET5K(spi, Pin(17), Pin(20))  # spi, cs, reset pin
    nic.active(True)
    
    # Static IP configuration
    nic.ifconfig(('192.168.137.100', '255.255.255.0', '192.168.137.1', '8.8.8.8'))
    
    # DHCP configuration
    # nic.ifconfig('dhcp')
    
    print('IP address:', nic.ifconfig())
    while not nic.isconnected():
        time.sleep(1)

def server_loop(): 
    s = socket()
    s.bind(('192.168.137.100', 5050))  # Source IP Address
    s.listen(5)
    
    print("TEST server")
    conn, addr = s.accept()
    print("Connected to:", conn, "address:", addr) 
    print("Loopback server Open!")
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if data != b'NULL':  # Use byte literal for comparison
            uart.write(data)  # Serial print
            conn.send(data)

def client_loop():
    s = socket()
    s.connect(('192.168.137.114', 5050))  # Destination IP Address
    
    print("Loopback client Connect!")
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != b'NULL':  # Use byte literal for comparison
            s.send(data)
        
def main():
    w5x00_init()
    
    ### TCP SERVER ###
    while True:
        server_loop()
    
    ### TCP CLIENT ###
    # client_loop()

if __name__ == "__main__":
    main()
