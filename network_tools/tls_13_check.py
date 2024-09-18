import ssl
import socket

def load() -> dict:
    host_dict = {}
    with open('hosts.txt', 'r') as hosts:
        for host in hosts:
            temp = host.strip('\n').split(',')
            host_dict[temp[0]] = temp[1]
    return host_dict

def check_tls():
    hostname = 'google.com'
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            for protocol in ssock.context.get_supported_protocols():
                print(protocol)

if __name__ == '__main__':
    hosts = load()
    check_tls()




