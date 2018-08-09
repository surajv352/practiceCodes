NUMBERS = '0123456789'

def increment(s):
    out = ''

    number = ''
    for c in s:
        if c in NUMBERS:
            number += c
        
        else:
            if number != '':
                out += str(int(number) + 1)
                number = ''
            out += c

    if number != '':
        out += str(int(number) + 1)
        number = ''


    return out

res = (increment('x0'))
print(res)