#1
'''
import re
def text_match(text):
    pattern='^a(b*)$'
    if re.search(pattern,text):
        return 'Found a match'
    else:
        return 'Not match'
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
'''




#2
'''
import re
def text_match(text):
    pattern='ab{2,3}'
    if re.search(pattern,text):
        return 'Found'
    else:
        return 'Not found'
print(text_match('ab'))
print(text_match('aabbbbbc'))
print(text_match('abb'))
'''




#3
'''
import re
def text_match(text):
    pattern='^[a-z]+_[a-z]+'
    if re.search(pattern,text):
        return 'Found'
    else:
        return 'Not found'
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))
'''




#4
'''
import re
def text_match(text):
    pattern='[A-Z]+[a-z]+$'
    if re.search(pattern,text):
        return 'Found'
    else:
        return 'Not Found'
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))
print(text_match('AAaaa'))
'''




#5
'''
import re
def text_match(text):
    pattern='a.*b$'
    if re.search(pattern,text):
        return 'True'
    else:
        return 'False'
print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))
print(text_match('abbccvdbfb'))
'''


#6
'''
import re
text='Python Exercices, PHP exercices.'
print(re.sub('[ ,.]',':',text))
'''



#7
'''
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))
'''



#8
'''
import re
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))
'''




#9
'''
import re
string='LetUsStudyPython'
words=re.findall('[A-Z][a-z]*',string)
print(' '.join(words))
'''





#10
import re

def func(word):
    return word.group("a")+ "_" + word.group("b").lower()

txt = "mySuperVar" 
x = "(?P<a>[a-z])(?P<b>[A-Z])+"

print(re.sub(x, func, txt))