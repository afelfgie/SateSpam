#!/usr/bin/env python
# -*- coding: utf-8 -*-
# jngn di recode anjink

import random
import time
import unittest

import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

def slowprint1(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.13)

#color
underlined='\033[04m'
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
lightgreen='\e[1;32m'
okegreen='\033[92m'
bold='\033[33;1m'

# Console colors
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

import os
import sys
import time
if sys.platform == "linux2":
        os.system("clear")
elif sys.platform == "win32":
        os.system("cls")
else:
        os.system("clear")
print "\033[35;1m"
os.system("figlet -f future SateSpam")
print
print """
\033[34;1m[===================================>
\033[92m [+]\033[33;1mAuthor \033[31m: \033[1;36mGunadiCBR
\033[92m [+]\033[33;1mCode   \033[31m: \033[1;36mpython
\033[92m [+]\033[33;1mTeam   \033[31m: \033[1;36mMls18hckr
\033[34;1m[===================================>"""
print
print "\033[33;1mSilahkan Pilih Tool Spammer Yang Kamu Mau Use"
print """
\033[34;1m~\033[31;1m{\033[01;33m01\033[31;1m}\033[34;1m~\033[37;1mJd.Id
\033[34;1m~\033[31;1m{\033[01;33m02\033[31;1m}\033[34;1m~\033[37;1mTelkomnyet
\033[34;1m~\033[31;1m{\033[01;33m03\033[31;1m}\033[34;1m~\033[37;1mTokopedia
\033[34;1m~\033[31;1m{\033[01;33m04\033[31;1m}\033[34;1m~\033[37;1mPHD
\033[34;1m~\033[31;1m{\033[01;33m05\033[31;1m}\033[34;1m~\033[37;1mHOOQ
\033[34;1m~\033[31;1m{\033[01;33m06\033[31;1m}\033[34;1m~\033[37;1mZIPAY
\033[34;1m~\033[31;1m{\033[01;33m07\033[31;1m}\033[34;1m~\033[37;1mWHISKAZ
\033[34;1m~\033[31;1m{\033[01;33m08\033[31;1m}\033[34;1m~\033[37;1mKFC
\033[34;1m~\033[31;1m{\033[01;33m09\033[31;1m}\033[34;1m~\033[37;1mLazada
\033[34;1m~\033[31;1m{\033[01;33m10\033[31;1m}\033[34;1m~\033[37;1mMatahari Mall
\033[34;1m~\033[31;1m{\033[01;33m11\033[31;1m}\033[34;1m~\033[37;1mEmail-Bomber
\033[34;1m~\033[31;1m{\033[01;33m99\033[31;1m}\033[34;1m~\033[37;1mInformasi Tool Ini
\033[34;1m~\033[01;32m{\033[01;33m00\033[01;32m}\033[34;1m~\033[1;36mKeluar"""

print R + " "
sate = raw_input ("\033[36;1mPilih Nomor \033[31m-->\033[36;1m\033[1m ")
if sate == '01' or sate == '1':
	os.system("clear")
	os.system('php jdid.php')
	sleep(2)
	restart_program()
if sate == '02' or sate == '2':
	os.system("clear")
	os.system('php telkomsel.php')
	sleep(2)
	restart_program()
if sate == '03' or sate == '3':
	os.system("clear")
	os.system('php lite.php')
	sleep(2)
	restart_program()
if sate == '04' or sate == '4':
	os.system("clear")
	os.system('php phd.php')
	restart_program()
if sate == '05' or sate == '5':
	os.system("clear")
	os.system('php hooq.php')
	sleep(2)
	restart_program()
if sate == '06' or sate == '6':
	os.system("clear")
	os.system('php zipay.php')
	restart_program()
if sate == '07' or sate == '7':
	os.system("clear")
	os.system('php whiskas.php')
	sleep(2)
	restart_program()
if sate == '08' or sate == '8':
	os.system("clear")
	os.system('php func.php')
	sleep(2)
	restart_program()
if sate == '09' or sate == '9':
	os.system("clear")
	os.system('python2 lazada.py')
	sleep(2)
	restart_program()
if sate == '10':
	os.system("clear")
	os.system('php mataharimall.php')
	sleep(2)
	restart_program()
if sate == '11':
	os.system("clear")
	os.system('python2 bombemail.py')
	sleep(2)
	restart_program
if sate == '99':
  os.system("clear")
  print "\033[37;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[31m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[34;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[36;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[33;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[35;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[37;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[31m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[34;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[36;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[33;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[35;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[37;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[31m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[34;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[36;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[33;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  os.system("clear")
  print "\033[35;1m"
  os.system("figlet SateSpam")
  sleep(0.03)
  print "\033[34;1m|============================================>"
  print "\033[1;33m[+]Nama Tool : \033[1;32mSateSpam"
  print "\033[01;33m[+]Author   : \033[1;32mGunadiCBR"
  print "\033[01;33m[+]Contack  : \033[1;32m085341899229"
  print "\033[01;33m[+]Version  : \033[1;32m1.2"
  print "\033[01;33m[+]Date     : \033[1;32m17-08-2018"
  print "\033[01;33m[+]code     : \033[1;32mpython"
  print "\033[01;33m[+]Github   : \033[1;32mhttp://github.com/afelfgie"
  print "\033[01;33m[+]Team     : \033[1;32mMls18Hckr"
  print "\033[34;1m|============================================>"
  print "\033[37;1m"
  slowprint1("Pencet \033[35;1mENTER \033[37;1mUntuk Kembali Ke Menu")
  key = raw_input(" ")
  os.system("python2 SateSpam.py")

if sate == '0' or sate == '00':
 os.system("clear")
 slowprint1("\033[36;1mBy...By...:)")
 sleep(1.20)
 os.system("clear")
 slowprint2("Exiting......................")
 print "\033[37;1m"
 print "##########"
 sleep(0.30)
 print "#########"
 sleep(.30)
 print "########"
 sleep(0.30)
 print "#######"
 sleep(0.30)
 print "######"
 sleep(0.30)
 print "#####"
 sleep(0.30)
 print "####"
 sleep(0.30)
 print "###"
 sleep(0.30)
 print "##"
 sleep(0.30)
 print "#"
 sleep(1)
 sys.exit()

else:
        print
        print R + "[!]WRONG INPUT[!]"
        time.sleep(0.40)
        restart_program()

KeyboardInterrupt


















