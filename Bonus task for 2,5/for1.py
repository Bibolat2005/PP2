#1
a=int(input())
b=int(input())
for i in range(a,b+1):
    print(i,end=' ')



#2
A = int(input())
B = int(input())
if A<B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)



#3
a = int(input())
b = int(input())
for i in range(a-int((a%2)==0), b-1, -2):
    print(i)



#4
n = int(input())
sum = 0

for i in range(n):
    i = int(input())
    sum += i
    
print(sum)




#5
n=int(input())
x=0
for i in range(1,n+1):
    x+=i**3
print(x)




#6
n=int(input())
x=1
for i in range(1,n+1):
    x=x*i
print(x)



#7
n=int(input())
x=1
sum=0
for i in range(1,n+1):
    x=x*i
    sum+=x
print(sum)




#8
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)




#9
n=int(input())
sum=0
for i in range(1,n+1):
    x=int(input())
    if x==0:
        sum+=1
print(sum)




#10
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,sep='',end='')
    print()





#11
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input())
print(sum)