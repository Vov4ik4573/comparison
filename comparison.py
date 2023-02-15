def compare(s):
    if s.find('>')!=-1:
        l=int(s[:s.find('>')])
        t=int(s[s.find('>')+1:])
        if(l>t):
            return True
        else:
            return False
    elif s.find('<')!=-1:
        l=int(s[:s.find('<')])
        t=int(s[s.find('<')+1:])
        if(l<t):
            return True
        else:
            return False
    else:
        return False

s=input()
print(compare(s))