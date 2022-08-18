from re import I


b = int(input())
i = 1
while i<=b :
    j = i 
    l = 1
    while l<=b :
        k = 64 + j 
        print(chr(k),end = " ")
        j = j + 1
        l = l + 1
    print()
    i = i + 1
    

# print this pattern 
# A B C D 
# B C D E
# C D E F
# D E F G
