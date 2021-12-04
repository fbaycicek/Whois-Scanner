#https://who.is/whois/{}
#IP = https://check-host.net/ip-info?host={}
#https://who.is/dns/{}

import requests
from time import sleep
from bs4 import BeautifulSoup

print(">>>Types of Query:  (1) Whois Query    (2) DNS Query    (3)IP Query")

work_number = input("Query Number?: ")
print("\n")
if work_number == '1':

    domain = input('>>[+]Enter a Domain: ')
    url = 'https://who.is/whois/{}'.format(domain)

    query = requests.get(url)
    sleep(5)
    soup = BeautifulSoup(query.content,'lxml')
    info = soup.find_all('div',attrs={'class':'col-md-12 queryResponseBodyValue'})
    file_name = input("Enter a File Name (example.txt): ")

    for inf in info:
        print(inf.text)
        data = inf.text
        write = data
        file = open(file_name,"a")
        ekle = file.write(write)
        file.close()
    print("File Saved / / Path: Program Files >>> ",file_name)

elif work_number == '2':

    domain = input('>>[+]Enter a Domain: ')
    url = 'https://who.is/dns/{}'.format(domain)

    query = requests.get(url)
    sleep(5)

    soup = BeautifulSoup(query.content,'lxml')
    info = soup.find_all('div',attrs={'class':'col-md-12 queryResponseBodyKey'})
    file_name = input("Enter a File Name (example.txt): ")

    for inf in info:
        print(inf.text)

        data = inf.text
        write = data
        file = open(file_name,"a")
        add = file.write(write)
        file.close()
    print("File Saved / / Path: Program Files >>> ",file_name)

elif work_number == '3':

    domain = input('>>[+]Enter a Domain: ')
    url = 'https://check-host.net/ip-info?host={}'.format(domain)

    query = requests.get(url)
    sleep(5)

    soup = BeautifulSoup(query.content,'lxml')
    info = soup.find_all('div',attrs={'class':'ipinfo-item'})
    file_name = input("Enter a File Name (example.txt): ")

    for inf in info:
        print(inf.text)

        data = inf.text
        write = data
        file = open(file_name,"a")
        add = file.write(write)
        file.close()
    print("File Saved / / Path: Program Files >>> ",file_name)

else:
    print("You Have Not Made a Valid Choice!")