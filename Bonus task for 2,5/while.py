#1
n=int(input())
i=1
while i**2<=n:
    print(i**2)
    i+=1



#2
n=int(input())
i=2
while n%i !=0:
    i+=1
print(i)



#3
n=int(input())
answer=1
i=0
while answer*2<=n:
    answer*=2
    i+=1
print(i,answer)



#4
x=int(input())
y=int(input())
i=1
while x<y:
    x=x*1.1
    i+=1
print(i)




#5
n=0
while int(input()) !=0:
    n+=1
print(n)


#6
sum=0
i=int(input())
while i !=0:
    sum+=i
    i=int(input())
print(sum)



#7
sum=0
len=0
element=int(input())
while element !=0:
    sum+=element
    len+=1
    element=int(input())
print(sum/len)



#8
a=int(input())
max=0
while a!=0:
    if a > max:
        max=a
    a=int(input())
print(max)



#9
e=int(input())
max=0
i=0
index=0
while e!=0:
    if e>max:
        max=e
        index=i
    e=int(input())
    i+=1
print(index)




#10
a=int(input())
index =0
i=0
while a!=0:
    if a%2==0:
        index+=1
    a=int(input())
print(index)




#11
prev=int(input())
answer=0
while prev!=0:
    next=int(input())
    if next!=0 and prev<next:
        answer+=1
    prev=next
print(answer)




#12
max1=0
max2=0
a=int(input())
while a != 0:
    if a>max1:
        max2=max1
        max1=a
    elif a>max2 :
        max2=a
    a=int(input())
print(max2)




#13
max=0
i=0
element=-1
while element!=0:
    element=int(input())
    if element>max:
        max,i=element,1
    elif element==max:
        i+=1
print(i)



#14
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)



#15
x=0
x1=1
x2=0
i=0
n=int(input())
while x<=n:
    x=x1+x2
    x1,x2=x,x1
    i+=1
if (n==x2):
    print(i)
else:
    print(-1)




#16
p=int(input())
c=1
b=0
while p!=0:
    v=int(input())
    p,v=v,p
    if v==p:
        c+=1
    if c>b:
        b=c
    if p!=v:
        c=1
print(b)




#17
from math import sqrt

partial_sum = 0
partial_sum_squares = 0
x_i = int(input())
n = 0
while x_i != 0:
    n += 1
    partial_sum += x_i
    partial_sum_squares += x_i ** 2
    x_i = int(input())
print(sqrt((partial_sum_squares - partial_sum ** 2 / n) / (n - 1)))
