import os
import socket
import time

def get_ipv4_address():
    try:
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        print("IPv4 Address:", ipv4_address)  # Debugging statement
        return ipv4_address
    except socket.gaierror:
        return None  # Return None if the IPv4 address is not available

def start_server(ipv4_address):
    os.system(f"cd C:\\web-logger-main && python manage.py runserver {ipv4_address}:8000")

def main():
    while True:
        ipv4_address = get_ipv4_address()
        if ipv4_address and ipv4_address != "127.0.0.1":
            print("Network connection established.")
            start_server(ipv4_address)
            break  # Break the loop if the IPv4 address is available and not localhost

        print("Waiting for network connection...")
        time.sleep(5)  # Wait for 5 seconds before checking again

    # Add this line to keep the command prompt window open until a key is pressed
    input("Press Enter to close...")

if __name__ == "__main__":
    main()
