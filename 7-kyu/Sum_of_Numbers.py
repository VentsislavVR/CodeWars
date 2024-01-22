def get_sum(a,b):
    return sum(x for x in range(min(a,b), max(a,b)+1)) if a != b else a


print(get_sum(1,0))