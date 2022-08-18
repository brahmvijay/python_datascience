from re import A


a = int(input())
i = 1
while i<=a :
    k = 1
    while k<=a :
        l = 64 + k
        print(chr(l),end = " ")
        k = k + 1
    print()
    i = i + 1 
# to print alphabet in python we have 2 methods 
#1.ord('A') --> it gives the ASCII value of the alphabet 
#2.chr(65) --> it gives the alphabet of the corresponding number 
#print this pattern 
# A B C D 
# A B C D
# A B C D
# A B C D