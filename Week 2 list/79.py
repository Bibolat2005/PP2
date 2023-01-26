thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
'''
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Отсортируйте список в зависимости от того, насколько число близко к 50:
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#По умолчанию sort()метод чувствителен к регистру, в результате чего все заглавные буквы сортируются перед строчными:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Сделайте копию списка с помощью list()метода:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)



'''