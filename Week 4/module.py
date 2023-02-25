import mymodule
mymodule.greeting("Jonathan")


import mymodule
a = mymodule.person1["age"]
print(a)


import mymodule as mx
a = mx.person1["age"]
print(a)


import platform
x = platform.system()
print(x)



import platform
x = dir(platform)
print(x)



from mymodule import person1
print (person1["age"])


#exercises:
#1
import mymodule

#2
import mymodule as mx

#3
import mymodule
print(dir(mymodule))

#4
from mymodule import person1
