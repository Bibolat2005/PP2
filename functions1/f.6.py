def reversed_str(string):
    split_str=string.split(' ')
    reversed_str=reversed(split_str)
    final_str=' '.join(reversed_str)
    return final_str
s=input()
k=reversed_str(s)
print(k)
