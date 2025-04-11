def swap_case(s):
    result=''
    for i in range(len(s)):
        if(s[i].isupper()):
            result+= s[i].lower()
        else:
            result += s[i].upper()
    return result

x=swap_case('SwapCase')
print(x)
