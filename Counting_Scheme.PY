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
ET = [  32, 1, 2, 3, 4, 5,\
        4, 5, 6, 7, 8, 9,\
        8, 9, 10, 11, 12, 13,\
        12, 13, 14, 15, 16, 17,\
        16, 17, 18, 19, 20, 21,\
        20, 21, 22, 23, 24, 25,\
        24, 25, 26, 27, 28, 29,\
        28, 29, 30, 31, 32, 1\
    ]
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

def expansion(inputString):                # returns the output of expansion box in binary form
    tmp = ''
    for i in ET:
        tmp = tmp + inputString[i-1]
    return tmp

def binaryXOR(inp1, inp2):                  # returns the XOR of two binary strings
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

S1keyCount=[];S2keyCount=[];
S3keyCount=[];S4keyCount=[];S5keyCount=[];S6keyCount=[];S7keyCount=[];S8keyCount=[];
for i in range(2**6):
    S1keyCount.append(0)
    S2keyCount.append(0)
    S3keyCount.append(0)
    S4keyCount.append(0)
    S5keyCount.append(0)
    S6keyCount.append(0)
    S7keyCount.append(0)
    S8keyCount.append(0)

EcharL2 = "00000000000000000000010000000000"
EcharL1 = "00000100000000000000000000000000"
InvpEcharL1 = InversPermFuncOutput(EcharL1)
InvpEcharL2 = InversPermFuncOutput(EcharL2)

fname = "Z1n.txt"
with open(fname) as f:
    content = f.readlines()
listZ1 = [x.strip() for x in content]

fname = "Z1starn.txt"
with open(fname) as f:
    content = f.readlines()
listZ2 = [x.strip() for x in content]

for j in range(len(listZ1)-1):
    Z1r = (listZ1[j])[32:64]
    Z1l = (listZ1[j])[0:32]
    Z1Starr = (listZ2[j])[32:64]
    Z1Starl = (listZ2[j])[0:32]
    ExpZ1r = expansion(Z1r)
    ExpZ1Starr = expansion(Z1Starr)
    cipher_xor = binaryXOR(Z1l, Z1Starl)
    Invpcipher_xor = InversPermFuncOutput(cipher_xor)
    # desiredOutLeft = binaryXOR(EcharL,cipher_xor)
    InvpdesiredOutLeft = binaryXOR(InvpEcharL1, Invpcipher_xor)

  #count of S1 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[0:6],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[0:6],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,1)
      sBoxOutput2=SBoxOutput(sBoxInput2,1)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[0:4]:     
          S1keyCount[i] += 1


  #count for S2 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[6:12],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[6:12],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,2)
      sBoxOutput2=SBoxOutput(sBoxInput2,2)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[4:8]:     
          S2keyCount[i] += 1

  #count of S3 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[12:18],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[12:18],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,3)
      sBoxOutput2=SBoxOutput(sBoxInput2,3)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[8:12]:     
          S3keyCount[i] += 1

  #count of S4 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[18:24],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[18:24],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,4)
      sBoxOutput2=SBoxOutput(sBoxInput2,4)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[12:16]:     
          S4keyCount[i] += 1

    #count for S5 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[24:30],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[24:30],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,5)
      sBoxOutput2=SBoxOutput(sBoxInput2,5)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[16:20]:
          S5keyCount[i] += 1

  #count for S6 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[30:36],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[30:36],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,6)
      sBoxOutput2=SBoxOutput(sBoxInput2,6)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[20:24]:
          S6keyCount[i] += 1

    #count for S7 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[36:42],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[36:42],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,7)
      sBoxOutput2=SBoxOutput(sBoxInput2,7)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[24:28]:
          S7keyCount[i] += 1

  #count for S8 key bits
    for i in range(2**6):
      sBoxInput1=binaryXOR(ExpZ1r[42:48],sixBitBinary(i))
      sBoxInput2=binaryXOR(ExpZ1Starr[42:48],sixBitBinary(i))
      sBoxOutput1=SBoxOutput(sBoxInput1,8)
      sBoxOutput2=SBoxOutput(sBoxInput2,8)
      if binaryXOR(sBoxOutput1,sBoxOutput2) == InvpdesiredOutLeft[28:32]:
          S8keyCount[i] += 1

partialkey = ''
k1 = S1keyCount.index(max(S1keyCount))
k2 = S2keyCount.index(max(S2keyCount))
k3 = S3keyCount.index(max(S3keyCount))
k4 = S4keyCount.index(max(S4keyCount))
k5 = S5keyCount.index(max(S5keyCount))
k6 = S6keyCount.index(max(S6keyCount))
k7 = S7keyCount.index(max(S7keyCount))
k8 = S8keyCount.index(max(S8keyCount))
partialkey = partialkey + bin(k1)[2:].zfill(6)+ " "+bin(k2)[2:].zfill(6)+" "+bin(k3)[2:].zfill(6) + " "+bin(k4)[2:].zfill(6)+" "+bin(k5)[2:].zfill(6) +" "+bin(k6)[2:].zfill(6)+" "+bin(k7)[2:].zfill(6)+" "+bin(k8)[2:].zfill(6)
# print(max(S1keyCount), " ", max(S2keyCount), " ", max(S3keyCount), " ", max(S4keyCount), " ", max(S5keyCount), " ", max(S6keyCount), " ")
# print(max(S7keyCount), " ", max(S8keyCount))
print(partialkey)