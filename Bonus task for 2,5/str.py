#1
st = str(input())
print(st[2])
print(st[-2])
print(st[:5])
print(st[:-2])
print(st[::2])
print(st[1::2])
print(st[::-1])
print(st[::-2])
print(len(st))



#2
st=input()
words=st.count(' ')
print(words+1)



#3
s=input()
n=len(s)
part_1=(s[:(n+(n%2))//2])
part_2=(s[(n+(n%2))//2:])
print(part_2+part_1)




#4
s = input()
a, b = s.split()
print(b + " " + a)



#5
s = input()
x = s.count('f')
if x == 1:
    print(s.find('f'))
elif x >= 2:
    print((s.find('f')), (s.rfind('f')))



#6
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))



#7
s = input()
print(s[:s.find('h')] + s[s.rfind('h') +1:])



#8
s = input()
a1 = s.find('h')
a2 = s.rfind('h')
x = s[a1 + 1:a2]
x = x[::-1]
print(s[:a1 + 1] + x + s[a2:])




#9
s=input()
print(s.replace(str(1),'one'))


#10
print(input().replace('@',''))


#11
s = input()
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
print(a + b.replace('h', 'H') + c)



#12
s=input()
for i in range(len(s)):
    if i%3 !=0:
        print(s[i],end='')