import socket
import requests

def port_scanner():
    print("\n======================")
    print(" Python Port Scanner ")
    print("======================")

    target = input("Enter target IP or domain: ").strip()

    common_ports = [
        21, 22, 23, 25,
        53, 80, 110,
        139, 143, 443,
        445, 3306, 8080
    ]

    print(f"\nScanning {target}...\n")

    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")

            sock.close()

        except KeyboardInterrupt:
            print("\nScan stopped.")
            break

        except:
            print("Error scanning.")
            break

    print("\nScan Complete.")


def ip_lookup():
    print("\n======================")
    print(" IP Geolocation Tool ")
    print("======================")

    ip = input("Enter IP Address: ").strip()

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        print("\nIP Information:")
        print(f"IP: {data.get('query')}")
        print(f"Country: {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"City: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Timezone: {data.get('timezone')}")

    except:
        print("Failed to fetch IP info.")


def dns_lookup():
    print("\n======================")
    print(" DNS Lookup Tool ")
    print("======================")

    domain = input("Enter domain: ").strip()

    try:
        ip = socket.gethostbyname(domain)

        print(f"\nDomain: {domain}")
        print(f"IP Address: {ip}")

    except:
        print("Failed to resolve domain.")


def reverse_dns():
    print("\n======================")
    print(" Reverse DNS Lookup ")
    print("======================")

    ip = input("Enter IP Address: ").strip()

    try:
        hostname = socket.gethostbyaddr(ip)

        print(f"\nHostname: {hostname[0]}")

    except:
        print("Reverse lookup failed.")


while True:
    print("\n======================")
    print(" Cyber Toolkit ")
    print("======================")

    print("1. Port Scanner")
    print("2. IP Geolocation")
    print("3. DNS Lookup")
    print("4. Reverse DNS Lookup")
    print("5. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":
        port_scanner()

    elif choice == "2":
        ip_lookup()

    elif choice == "3":
        dns_lookup()

    elif choice == "4":
        reverse_dns()

    elif choice == "5":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")
