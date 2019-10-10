def My_split(ipt, sep):
    result = []
    help = ''
    for e in ipt:
        if e != sep:
            help += e
        elif help != '': # e == sep
            result.append(help)
            help = '' # Reset the helper character
    if help != '':
        result.append(help)
    return result
ipt = input()
sep = ' ' # You can choice the separator. Exemple: ",", " ", "."
My_split = My_split(ipt, sep)
print(My_split)
