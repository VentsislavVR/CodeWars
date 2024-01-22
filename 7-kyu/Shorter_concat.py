def shorter_reverse_longer(a, b):
    if len(a) != len(b):
        shorter_str = min(a, b, key=len)
        longer_str = max(a, b, key=len)
    else:
        shorter_str, longer_str = b, a

    return shorter_str + longer_str[::-1] + shorter_str


print(shorter_reverse_longer('i', 'y'))
