import subprocess

def check_tls_with_openssl(hostname, port=443):
    tls_versions = {
     #   "TLSv1.0": "tls1",
    #    "TLSv1.1": "tls1_1",
        "TLSv1.2": "tls1_2",
        "TLSv1.3": "tls1_3"
    }
    
    supported_versions = []

    for version_name, openssl_flag in tls_versions.items():
        command = f"openssl s_client -crlf -connect {hostname}:{port} -servername {hostname} -{openssl_flag}"
        # openssl s_client -crlf -connect krokowa.pl:443 -servername krokowa.pl -tls1_2
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=2)
            print(result.stdout.lower())
            if ("no peer certificate") not in result.stdout.lower():
                print(f"{version_name} is supported by {hostname}")
                supported_versions.append(version_name)
            else:
                print(f"{version_name} is NOT supported by {hostname}")
        except subprocess.TimeoutExpired:
            print(f"Connection timed out for {version_name}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    return supported_versions

# Example usage
hostname = 'krokowa.pl'
supported_tls_versions = check_tls_with_openssl(hostname)
print(f"Supported TLS versions for {hostname}: {supported_tls_versions}")
