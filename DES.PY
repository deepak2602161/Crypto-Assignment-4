#S-Boxes
S = [\
  [14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7],\
  [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],\
  [4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0],\
  [15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13],\
  \
  [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10],\
  [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],\
  [0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15],\
  [13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9],\
  \
  [10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8],\
  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],\
  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7],\
  [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],\
  \
  [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],\
  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],\
  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4],\
  [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],\
  \
  [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],\
  [14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],\
  [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],\
  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],\
  \
  [12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11],\
  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],\
  [9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],\
  [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],\
  \
  [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],\
  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],\
  [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],\
  [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],\
  \
  [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7],\
  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],\
  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],\
  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]\
    ]
#expansion box
ET = [  32, 1, 2, 3, 4, 5,\
        4, 5, 6, 7, 8, 9,\
        8, 9, 10, 11, 12, 13,\
        12, 13, 14, 15, 16, 17,\
        16, 17, 18, 19, 20, 21,\
        20, 21, 22, 23, 24, 25,\
        24, 25, 26, 27, 28, 29,\
        28, 29, 30, 31, 32, 1\
    ]
#permutation function
funcP = [ 16, 7, 20, 21,\
          29, 12, 28, 17,\
          1, 15, 23, 26,\
          5, 18, 31,10,\
          2, 8, 24, 14,\
          32, 27, 3, 9,\
          19, 13, 30, 6,\
          22, 11, 4, 25,\
        ]
#inverse of the permutation function of Sbox
invP = [\
  9, 17, 23, 31,\
  13, 28, 2, 18,\
  24, 16, 30, 6,\
  26, 20, 10, 1,\
  8, 14, 25, 3,\
  4, 29, 11, 19,\
  32, 12, 22, 7,\
  5, 27, 15, 21,\
      ]
#Initial Permutation
InitialP = [\
  58,50,42,34,26,18,10,2,\
  60,52,44,36,28,20,12,4,\
  62,54,46,38,30,22,14,6,\
  64,56,48,40,32,24,16,8,\
  57,49,41,33,25,17,9,1,\
  59,51,43,35,27,19,11,3,\
  61,53,45,37,29,21,13,5,\
  63,55,47,39,31,23,15,7\
     ]
# Final Permutation
FinalP = [\
  40,8,48,16,56,24,64,32,\
  39,7,47,15,55,23,63,31,\
  38,6,46,14,54,22,62,30,\
  37,5,45,13,53,21,61,29,\
  36,4,44,12,52,20,60,28,\
  35,3,43,11,51,19,59,27,\
  34,2,42,10,50,18,58,26,\
  33,1,41,9,49,17,57,25\
     ]

PC1 = [\
  57, 49, 41, 33, 25, 17, 9,
  1, 58, 50, 42, 34, 26, 18,
  10,  2, 59, 51, 43, 35, 27,
  19, 11,  3, 60, 52, 44, 36,
  63, 55, 47, 39, 31, 23, 15,
  7, 62, 54, 46, 38, 30, 22,
  14,  6, 61, 53, 45, 37, 29,
  21, 13,  5, 28, 20, 12,  4
]

shifts = [\
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1\
          ]

PC2 = [\
  14, 17, 11, 24,  1, 5, 
  3, 28 ,15,  6, 21, 10, 
  23, 19, 12,  4, 26, 8, 
  16,  7, 27, 20, 13, 2, 
  41, 52, 31, 37, 47, 55, 
  30, 40, 51, 45, 33, 48, 
  44, 49, 39, 56, 34, 53, 
  46, 42, 50, 36, 29, 32
]
# map between subkey k6 and DES 56 bit key 
k_k6 = [\
	24, 27, 21, 6, 11, 15, 
	13, 10, 25, 16, 3, 20, 	
	5, 1, 22, 14, 8, 18, 
	26, 17, 9, 2, 23, 12, 
	51, 34, 41, 47, 29, 37,
	40, 50, 33, 55, 43, 30, 
	54, 31, 49, 38, 44, 35, 
	56, 52, 32, 46, 39, 42
]
key56 = list("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")   # 56 bit DES key initialised
subkey = list("000111100000xxxxxx110110010011011010110011100101")          # subkey k6 after implementing counting scheme

for i in range(48):                    #                 
	key56[k_k6[i]-1] = subkey[i]
key = ''.join(key56)
# print(key)

def generateKeyAfterPC1(k):         #generates 56 bit key for DES
    tmp = ''
    for i in PC1:
        tmp = tmp + k[i-1]
    return tmp

# desKey = generateKeyAfterPC1()     #the 56bit key you'll have

# C = []                             #list of C and D blocks  
# D = []
# C.append(key[0:28])
# D.append(key[28:56])

def leftShiftKey(keyBits, offset):
	tmp = ''
	for i in range(len(keyBits)-offset):
		tmp = tmp + keyBits[i+offset]
	if offset == 2:
		tmp = tmp + keyBits[0]
		tmp = tmp + keyBits[1]
	else:
		tmp = tmp + keyBits[0]
	return tmp

                      # list of all round keys 
def roundkeys(n, key):
	RoundKeys = [] 
	C = []                             #list of C and D blocks  
	D = []
	C.append(key[0:28])
	D.append(key[28:56])
	for i in range(n):
		left = C[i]
		right = D[i]
		offset = shifts[i]
		C.append(leftShiftKey(left, offset))
		D.append(leftShiftKey(right, offset))
		tmp = C[i+1] + D[i+1]
		tmp1 = ''
		for i in PC2:
			tmp1 = tmp1 + tmp[i-1]
		RoundKeys.append(tmp1)
	return RoundKeys

# n = input("input the number of rounds")			 
# roundkeys(int(n))

def IP(inputString):
    tmp = ''
    for i in InitialP:
        tmp = tmp + inputString[i-1]
    return tmp

def FP(inputString):
    tmp = ''
    for i in FinalP:
        tmp = tmp + inputString[i-1]
    return tmp

def expansion(inputString):
    tmp = ''
    for i in ET:
        tmp = tmp + inputString[i-1]
    return tmp
   
def binaryXOR(inp1, inp2):                  #returns the XOR of two binary strings
    tmp = ''
    tmp = int(inp1,2)^int(inp2,2)
    return bin(tmp)[2:].zfill(len(inp2))

def bin_to_dec(bin_string):
	out = 0
	bin_length = len(bin_string)
	for i in range(0, bin_length):
		out = out + pow(2, i)*int(bin_string[-(i+1)])
	return out

def SBoxOutput(SboxInp, boxNo):                 #returns the S-box output in binary form  
    r = SboxInp[0] + SboxInp[5]					#SboxInp is is binary form	
    c = SboxInp[1:5]
    row = bin_to_dec(r)
    column = bin_to_dec(c)
    a = S[row + 4*(boxNo-1)][column]
    b = bin(a)[2:].zfill(4)
    return b

def PermFuncOutput(binaryString):
    tmp = ''
    for i in funcP:
        tmp = tmp + binaryString[i-1]
    return tmp

def InversPermFuncOutput(binaryString):
    tmp = ''
    for i in invP:
        tmp = tmp + binaryString[i-1]
    return tmp

def sixBitBinary(decimal):
    return bin(decimal)[2:].zfill(6)

def conversion(ch):
	return ord(ch)-ord('f')

def char_to_bin(inputstring):
	tmp = ''
	for i in inputstring:
		tmp = tmp + bin(conversion(i))[2:].zfill(4)
	return tmp

def getFfuncOutput(roundinput, roundNo, RoundKeys):     # get output of any round in binary form
    expPlain = expansion(roundinput)
    r = RoundKeys[roundNo-1]
    sBoxinput = binaryXOR(expPlain, r) 
    sOutput = ''
    for i in range(8):
    	a = SBoxOutput(sBoxinput[6*i:6*(i+1)], i+1)
    	sOutput = sOutput + a
    return PermFuncOutput(sOutput)        	

def DES(inputstring, ed, n, key):      # DES calculater; ed = 1 for encryption and -1 for decryption
	Rkeys = roundkeys(n, key)
	plainBin = char_to_bin(inputstring)
	IPplain = IP(plainBin)
	L = []               # list of inputs and outputs of different rounds
	R = []
	L.append(IPplain[0:32])   # L0, R0
	R.append(IPplain[32:64])
	if ed == -1:
		Rkeys.reverse()
	for i in range(6):         # computation of different rounds
		L.append(R[i])
		r = R[i]
		l = L[i]
		r1 = getFfuncOutput(r, i+1, Rkeys)
		R.append(binaryXOR(r1, l))
	cipherbin = R[-1] + L[-1]  # final output of all rounds
	FPcipherbin = FP(cipherbin) # final plaintext/ciphertext in binary
	a = FPcipherbin
	output = ''
	for i in range(16):         # converting plaintext/ciphertext from binary to character form
		tmp = a[4*i:4*i+4]
		n = bin_to_dec(tmp)
		ch = chr(102+n)
		output = output + ch
	return output	

def bruteforce(inputString, outputString, key):
	for i in range(2**14):
		i1 = bin(i)[2:].zfill(14)
		keycomplete = list(key);
		t = 0;
		for j in range(56):
			if(keycomplete[j] == 'x'):
				keycomplete[j] = i1[t]
				t = t+1
		if DES(inputString, 1, 6, ''.join(keycomplete)) == outputString: 
			return ''.join(keycomplete);
	return -1;	

def convert2ASCII(string):
    s = ""
    for i in range(0,len(string),2):
        n = 16*(ord(string[i]) - ord('f')) + (ord(string[i+1]) - ord('f'))
        s += chr(n)
        print(n, end=" ")
    return s

# finalkey = bruteforce("ffffffffffffffff", "ghirlfsohhkhisfk", key)
# finalkey = "11001110001010101000011001011010111010000111110101001101"
# print(DES("ufitmnsjfkpuuqoq", 1, 6, finalkey))
# a= convert2ASCII("lgmilnlkmgmflrmhmllgifififififif")
# print(finalkey)