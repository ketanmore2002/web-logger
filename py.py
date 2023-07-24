import os
import socket

def get_ipv4_address():
    try:
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        print("IPv4 Address:", ipv4_address)  # Debugging statement
        return ipv4_address
    except socket.gaierror:
        return '127.0.0.1'  # Use localhost as the default IP address

def main():
    ipv4_address = get_ipv4_address()
    os.system(f"cd C:\\web-logger-main && python manage.py runserver {ipv4_address}:8000")
    
    # Add this line to keep the command prompt window open until a key is pressed
    input("Press Enter any key to close...")

if __name__ == "__main__":
    main()
