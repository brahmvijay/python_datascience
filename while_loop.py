# this is the python code of finding sum of even numbers till n 
k = int(input())
count = 1
sum = 0
while count<=k :
    if count % 2 ==0 :
        sum = sum + count
    count = count +1

print(sum)
