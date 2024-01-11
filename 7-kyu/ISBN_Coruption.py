def fix_code(isbn):
    total = 0

    for i, digit in enumerate(isbn):
        if digit == '?':
            if i == len(isbn) - 1:
                total += 10
            else:
                total += (10 - i) * int(isbn[i - 1])
        else:
            total += (10 - i) * int(digit)

    remainder = total % 11
    missing_digit = (11 - remainder) % 11

    if missing_digit == 10:
        return 'X'
    else:
        return str(missing_digit)


print(fix_code('02?1103311'))