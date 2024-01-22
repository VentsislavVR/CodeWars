def gimme_the_letters(sp):
    start , end = sp.split('-')
    return ''.join(chr(x) for x in range(ord(start),ord(end)+1))



print(gimme_the_letters("A-Z"))