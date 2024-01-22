def high_and_low(numbers):
    high,low = max(int(x) for x in numbers.split()),min(int(x) for x in numbers.split())
    # ...
    return f'{high} {low}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))