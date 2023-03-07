#1
'''
import os
f="C:\\Users\\Биболат\\Desktop\\PP2\\week 6"
for root, directories, files in os.walk(f):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)
'''


#2
'''
import os
print('Exist:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.F_OK))
print('Readable:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.R_OK))
print('Writable:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.W_OK))
print('Executable:', os.access("C:\\Users\\Биболат\\Desktop\\PP2\\week 6", os.X_OK))
'''



#3
'''
import os
phonk="C:\\Users\\Биболат\\Desktop\\PP2\\week 6"
print(os.path.exists(phonk))
print(os.path.basename(phonk))
print(os.path.dirname(phonk))
'''


#4
'''
f=open("C:\\Users\\Биболат\\Desktop\\PP2\\demofile2.txt","r")
lines=len(f.readlines())
print(lines)
'''


#5
'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())
'''




#6
'''
for i in range(65,91):
    file=open(chr(i)+".txt","w")
'''


#7
'''
with open("first.txt",'r') as firstfile,open("second.txt",'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
'''



#8
'''
import os
path="C:\\Users\\Биболат\\Desktop\\PP2\\week 6"
if os.path.exists(path):
    os.remove(path)
else:
    print('File does not exist')
'''