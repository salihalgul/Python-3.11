# x = 1
# y = 1
# z = 1
# n = 2

# print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])

# x = 2
# y = 2
# z = 2
# n = 2

# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k != n))

import math
import os
import random
import re
import sys

n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and (n >= 2 and n < 6):
    print("Not Weird")
elif n % 2 == 0 and (n > 6 and n < 21):
    print("Weird")
else:
    print("Not Weird")