from pwn import *
import sys

if len(sys.argv) != 2:
	print("Invalid arguments!")
	print(f">> {sys.argv[0]} <sha256sum>")
	exit()

wanted_hash = sys.argv[1]
password_file = "passwords2.txt"
attempts = 0

# pwntools log progress
with log.progress("Attempting to crack: {}\n".format(wanted_hash)) as p:
	with open(password_file, "r", encoding="latin-1") as password_list:
		for password in password_list:
			password = password.strip("\n").encode("latin-1")
			#print(password)
			password_hash = sha256sumhex(password)
			#print(password_hash)
			p.status("[{}] {} == {}".format(attempts, password.decode("latin-1"), password_hash))
			if password_hash == wanted_hash:
				p.success("Password hash found after {} attempts! {} hashes to {}".format(attempts,password.decode("latin-1"), password_hash))
				exit()
			attempts += 1
		p.failure("Password hash not found!")