#1
'''
def multiply(numbers):
    total=1
    for x in numbers:
        total*=x
    return total
print(multiply((1,2,3,4,5)))
'''


#2
'''
s=input()
cnt_upper=0
cnt_lower=0
for i in s:
    if i.isupper():
        cnt_upper+=1
    if i.islower():
        cnt_lower+=1
print(cnt_upper)
print(cnt_lower)
'''


'''
#3
s=str(input())
t=s[::-1]
if s==t:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
'''



#4
'''
import math
import time

num = int(input())
millisec = int(input())

time.sleep(millisec / 1000)

ans = math.sqrt(num)

print(f"Square root of {num} after {millisec} milliseconds is {ans}.")
'''



#5
'''
mytuple = (True, True, False)
x = all(mytuple)
print(x)
'''