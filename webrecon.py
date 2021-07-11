import requests
import sys
import pyfiglet


def subdomains():
    with open("files/subdmainwordlist.txt", "r") as subd:
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
    with open("files/directory.txt", "r") as dirlist:
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
    try:
        option = int(input("\nChoose 1 or 2: "))
        if option == 1:
            print("<----------------Checking for Subdomains---------------->")
            subdomains()
        elif option == 2:
            print("<----------------Checking for Directories---------------->")
            directories()
        else:
            print("\n<----------Choose Correct Option---------->\n")
            start()
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("\n<----------Choose Correct Option---------->\n")
        start()


print(pyfiglet.figlet_format("Webrecon"))
print("By: Tanish Mahajan")

url = input("\nEnter the Domain Name (For example: google.com, yahoo.com): ")
try:
    checkurl = requests.get("http://www." + url)
    start()
except requests.exceptions.ConnectionError:
    print("Incorrect Domain name")

