# this is the python code of finding sum of even numbers till n 
# k = int(input())
# count = 1
# sum = 0
# while count<=k :
#     if count % 2 ==0 :
#         sum = sum + count
#     count = count +1

# print(sum)

# python code for prime number or not 
m = int(input())
count = 2
k = 0
while m>count :
    if m % count == 0 :
        k = k + 1
    
    count = count + 1
if k>0 : 
    print("not prime")
else :
    print("prime")