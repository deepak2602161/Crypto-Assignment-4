import pyautogui
import random
import string
import numpy as np
#screenWidth, screenHeight = pyautogui.size()
def initialPerm(string):
    IP = np.array([58,50,42, 34,26,18,10,2,60,52,44,36,28,20,12,4,62,54, 46, 38, 30, 22, 14,6, 64, 56, 48, 40,32,24, 16, 8,57, 49, 41, 33,25,17, 9,1,59, 51,43,35,27,19,11,3,61,53,45,37,29,21,13, 5,63,55, 47,39,31,23,15,7])
    IP = IP-1
    PermString = ""
    for i in range(len(string)):
        PermString += string[IP[i]]
    return PermString;
def finalPerm(string):
    FP = np.array([40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25])
    FP = FP-1
    PermString = ""
    for i in range(len(string)):
        PermString += string[FP[i]]
    return PermString;
def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def random64bit():
    return random_generator(64, "01")
def convertBinary2Alpha(string):
    s = ""
    for i in range(0, len(string), 4):
        s += chr(int("0b" + string[i:i+4], 0) + ord('f'));
    return s;
def convertAlpha2Binary(string):
    s = ""
    for c in string:
        i = ord(c) - ord('f')
        temp = "{0:b}".format(i + 16)
        s += temp[1:]
    return s
def getCipher(string):
    #pyautogui.position()
    pyautogui.moveTo(35, 175)
    pyautogui.click()
    pyautogui.moveTo(1237,701)
    pyautogui.click()
    pyautogui.typewrite(string)
    pyautogui.press('enter')
    pyautogui.moveTo(220,630)
    pyautogui.dragTo(920, 630, button='left')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.moveTo(20, 470)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
# Used to generate random strings
'''
f = open('X1.txt', 'w')
for i in range(500):
    f.write(random64bit()+'\n')  # python will convert \n to os.linesep
f.close()
'''
# Used to generate X* = X xor X'
'''
fname = "X1.txt"
with open(fname) as f:
    content = f.readlines()
list = [x.strip() for x in content]
sigma1 = int("0b"+"0100000000001000000000000000000000000100000000000000000000000000", 0)
f = open('X1*.txt', 'w')
for line in list:
    s = (int("0b"+line,0))^sigma1
    f.write('{0:064b}'.format(s) +'\n')  # python will convert \n to os.linesep
f.close()
sigma2 = int("0x"+"00200008400400", 0)
f = open('X2*.txt', 'w')
for line in list:
    s = (int("0b"+line,0))^sigma2
    f.write('{0:064b}'.format(s) +'\n')  # python will convert \n to os.linesep
f.close()
'''
'''
# Used to get Y = encrypt(FP(X))
fname = "X2*.txt"
with open(fname) as f:
    content = f.readlines()
list = [x.strip() for x in content]
pyautogui.PAUSE = 0.1
for word in list:
    getCipher(convertBinary2Alpha(finalPerm(word)))
pyautogui.hotkey('ctrl', 's')
'''

# Used to get Z = IP(Y)

fname = "Y2*.txt"
with open(fname) as f:
    content = f.readlines()
list = [x.strip() for x in content]
f = open('Z2*.txt', 'w')
for line in list:
    f.write(initialPerm(convertAlpha2Binary(line)) +'\n')  # python will convert \n to os.linesep
f.close()
