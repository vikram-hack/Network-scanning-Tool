import socket
import concurrent.futures
import sys
import time

def resolve_host(host):
    try:
        return socket.gethostbyname(host)
    except:
        print(f"Error resolving host {host}")
        return None

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                # Banner grabbing
                try:
                    sock.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
                    banner = sock.recv(1024).decode().strip()
                except:
                    banner = None
                return port, banner
            else:
                return None
    except:
        return None

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"

def main():
    host_input = input("Enter IP address or domain name to scan: ").strip()
    ip = resolve_host(host_input)
    if not ip:
        print("Could not resolve host.")
        sys.exit(1)

    scan_type = input("Scan type ('basic' 1-1024 or 'aggressive' 1-65535): ").strip().lower()
    if scan_type == 'basic':
        ports = range(1, 1025)
    elif scan_type == 'aggressive':
        ports = range(1, 65536)
    else:
        print("Invalid input, defaulting to basic scan.")
        ports = range(1, 1025)

    print(f"Scanning {ip} ports from {ports.start} to {ports.stop - 1} ...")
    start_time = time.time()

    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                port, banner = result
                service_name = get_service_name(port)
                open_ports.append({'port': port, 'service': service_name, 'banner': banner})

    elapsed = time.time() - start_time
    print(f"\nScan completed in {elapsed:.2f} seconds.\n")

    if open_ports:
        print(f"{'Port':<6} {'Service':<15} {'Banner'}")
        print("-" * 60)
        for entry in sorted(open_ports, key=lambda x: x['port']):
            banner = entry['banner'] if entry['banner'] else "-"
            print(f"{entry['port']:<6} {entry['service']:<15} {banner}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
