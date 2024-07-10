import socket
import sys


def tcp_port_scanner(host:str, port_range:list):
    open_ports = []
    print(f"[*] Scanning ports {port_range[0]}:{port_range[-1]}")

    for port in port_range:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        try:
            result = client.connect((host, port))
            open_ports.append(port)
        except ConnectionRefusedError:
            pass
        except TimeoutError:
            pass
        except KeyboardInterrupt:
            print("[*] Keyboard interrupt")
            client.close()
            sys.exit()

        client.close()
    
    print(f"[*] Open ports: {open_ports}")

# not finished
def udp_port_scanner(host:str, port_range:list):
    print(f"[*] Scanning ports {port_range[0]}:{port_range[-1]}")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(2.0)
    open_udp_ports = []

    for port in port_range:
        try:
            print(f"[*] Scanning port {port}")
            client.sendto(b"SYN", (host,port))
            client.settimeout(1)
            data, addr = client.recvfrom(16)
            if len(data) > 0:
                open_udp_ports.append(port)
                print(f"[*] Port {port} OPEN")
        except socket.timeout:
            pass
        except KeyboardInterrupt:
            print("[*] Exiting...")
            client.close()
            sys.exit()
    

    print(f"[*] Open ports: {open_udp_ports}")

if __name__ == "__main__":
    host = '10.0.0.1'
    port_range = list(range(20,444))
    tcp_port_scanner(host, port_range)