# Simple program that sends a morse code message via a phillips hue
# lamp.

import time
import urllib
import urllib2

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

ON = "{\"on\":true, \"bri\":254}"
OFF = "{\"on\":false, \"bri\":254}"

class HueUpdater:
    def __init__(self, user):
        self.user = user

    def update(self, data):
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        url = "http://10.0.1.2/api/%s/lights/1/state/" % self.user
        request = urllib2.Request(url=url, data=data)
        request.get_method = lambda: 'PUT'
        opener.open(request)
        time.sleep(0.2)    
    
def morse(updater, char):
    if char == ' ':
        time.sleep(3.5)
        return

    code = CODE[char.upper()]
    for x in code:
        if x == '.':
            updater.update(ON)
            time.sleep(0.2)
            updater.update(OFF)
        else:
            updater.update(ON)
            time.sleep(1.0)
            updater.update(OFF)
        time.sleep(0.2)
    time.sleep(1.0)

def main():
    user = raw_input("Enter username: ")
    string = raw_input("Enter string to codify: ") 
    print "OK, codifying %s" % string
    updater = HueUpdater(user)
    updater.update(OFF)
    time.sleep(1.0)
    for char in string:
        morse(updater, char)
    print "All done!"

if __name__ == "__main__":
    main()
