import urllib.parse
import urllib.request

# send a HTTP GET
def http_get():
    url = 'https://ratels.pl'
    with urllib.request.urlopen(url) as response:
        content = response.read()

    print(content)

# send a HTTP POST
def http_post():
    info = {"user": "tim", "passwd": "31337"}
    data = urllib.parse.urlencode(info).encode()

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = reponse.read()
    
    print(content)

if __name__ == "__main__":
    http_get()