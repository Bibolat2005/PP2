'''
#1
def gensquares(n):
    for i in range(n):
        yield i**2
for x in gensquares(int(input())):
    print(x)


n=int(input())
a=(i**2 for i in range(1,n,1))
for i in a: 
    print(i)
'''

#2
'''
def even_numbers(n):
    for i in range(1,n+1,1):
        if i%2==0:
            print(i)
even_numbers(int(input()))


n=int(input())
a=[i for i in range(0,n+1,2)]
print(a)



def gen_even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(input())
values=[]
for i in gen_even(n):
    values.append(str(i))
print(','.join(values))
'''
'''
#3
def divisible_nums(n):
    for i in range(1,n+1,1):
        if i%3==0 and i%4==0:
            print(i)
divisible_nums(int(input()))


n=int(input())
a=[i for i in range(0,n+1,1) if i%12==0]
print(a)
'''


#4
'''
def square(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
for i in square(a,b):
    print(i)
'''


#5
'''
n=int(input())
a=[i for i in range(n,-1,-1)]
print(a)
'''

def decr_num(n):
    for i in range(n,-1,-1):
        print(i)
decr_num(int(input()))