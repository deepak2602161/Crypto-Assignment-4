import numpy as np
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

def leftShiftKey(keyBits, offset):
  k = np.zeros(28)
  for i in range(28):
    k[(i-offset)%28] = keyBits[i]
  return k;

def pc2(key):
    tmp = ''
    for i in PC2:
        tmp = tmp + str(int(key[i-1])) + ", "
    return tmp

a = np.zeros(56)
C = np.zeros(28)
R = np.zeros(28)
for i in range(56):
  a[i] = i+1
C = a[0:28]
R = a[28:56]
# print(C)

for i in range(6):
  C = leftShiftKey(C, shifts[i])
  R = leftShiftKey(R, shifts[i])
# print(C)
key = np.zeros(56)
key[0:28] = C
key[28:56] = R
keyFinalPermutation = pc2(key)
print(keyFinalPermutation)



