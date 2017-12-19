#!/usr/bin/python3

import os
from threading import Thread
import time
from subprocess import check_output


class Wicrack(object):
    """Main class of the program"""
    __author__ = 'piper'
    __version__ = 0.1

    def info():
        print(" Wicrack v{}".format(Wicrack.__version__))
        print(" By {}".format(Wicrack.__author__))
        print(" git: https://github.com/piperjames/wicrack.git")

    menu_options = {-1: {-1: 'Select Job',
                        1: {'Wifi': {1: ['self.interface()'],
                                     0: 'Back<<'}},
                        2: {'WebApp':   {-1: 'Select Attack Method',
                                     1: 'SQL Injection (SQLi)',
                                     2: 'Cross Site Scripting (Xss)',
                                     3: 'Cross Site Request Forgery (CRSF)',
                                     4: 'Content Spoofing',
                                     5: 'Clickjacking',
                                     6: 'Tabnabbing',
                                     7: 'Denial of Service',
                                     8: 'Man-In-The-Browser',
                                     9: 'Phishing',
                                     0: 'Back<<'}
                            },
                        3: {'Network':  {-1: 'Select Attack Method',
                                     1: 'Bruteforcing',
                                     2: 'Man-In-The-Middle',
                                     3: 'Buffer Overflow',
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
                print(".:%s:."%self.current_menu[key])
            elif str(key).isalpha():
                for opt in self.current_menu[key].keys():
                    if opt == -1:
                        print(".:%s:."%self.current_menu[key][opt])
                    elif opt == 0:
                        print(" [%d] %s"%(opt, self.current_menu[key][opt]))
                    else:
                        if len(self.current_menu[key][opt]) == 1:
                            self.current_menu[key][opt] = eval(self.current_menu[key][opt][0])
                        print(" [%d] %s"%(opt, self.current_menu[key][opt]))
            else:
                for opt in self.current_menu[key].keys():
                    print(" [%d] %s"%(key, opt))
        print("")
        while True:
            try:
                job = int(input("-|Choose Option| "))
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
                #time.sleep(1)
                print('\nGoodbye :)')
                #time.sleep(1)
                print('Exiting...')
                #time.sleep(1)
                exit(1)
            except Exception as e:
                print(str(e))
                continue

    def interface(self, iface='wlan0'):
        inface = input('Enter Interface to use [wlan0]: ')
        if not inface:
            inface = iface
        return inface


if __name__ == "__main__":
        Wicrack()

#Thread(target=capture_handshake, args=('BE:B3:08:CC:58:C5', 1)).start()
#Thread(target=deauthenticate, args=('BE:B3:08:CC:58:C5', 1)).start()
