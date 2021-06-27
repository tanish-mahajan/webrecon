import requests
import sys

url = input("Enter the Domain Name: ")


def subdomains():
    with open("subdmainwordlist.txt", "r") as subd:
        for line in subd:
            word = line.strip()
            testurl = word + "." + url
            try:
                response = requests.get("http://" + testurl)
            except requests.exceptions.ConnectionError:
                pass
            except KeyboardInterrupt:
                sys.exit()
            if response:
                print("[+] Subdomain Discovered --> " + testurl)


def directories():
    with open("directory.txt", "r") as dirlist:
        for dir in dirlist:
            # print(dir)
            word = dir.strip()
            testurl = "http://www." + url + "/" + word
            try:
                response = requests.get(testurl)
            except requests.exceptions.ConnectionError:
                pass
            except KeyboardInterrupt:
                sys.exit()
            if response:
                print("[+] Directory Discovered --> " + testurl)


def start():
    print("1. Subdomains\n2. Directories")
    option = int(input("Choose 1 or 2: "))
    if option == 1:
        print("<----------------Checking for Subdomains---------------->")
        subdomains()
    elif option == 2:
        print("<----------------Checking for Directories---------------->")
        directories()
    else:
        print("Choose Correct Option")
        start()


start()
