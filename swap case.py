def swap_case(s):
    l=''
    for a in s:
        if (a.isupper()):
            l=l+a.lower()
        else:
            l=l+a.upper()
            
    return l

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
