s= 'this is the string'

def split(s):
    split=s.split(' ')
    split='-'.join(split)
    return split

x=split(s)
print(x)