#!/usr/bin/python
string = input()
str1 = ''
for i in string:
    str1 = i + str1
print(str1)
str2 = list(str1)
for i in range(len(str2)):
    if str2[i] == 'A':
        str2[i]='T'
    elif str2[i] == 'C':
        str2[i]='G'
    elif str2[i] == 'T':
        str2[i]='A'
    else:
        str2[i]='C'
s = str2
str3 = ''
str4 = ''
for i in s:
    str3 = i + str3
for i in str3:
    str4 = i + str4
print(str4)
