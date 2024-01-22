def freed_prisoners(cells):
    if not cells or not cells[0]:
        return 0

    count = 0
    locked = False

    for cell in cells:
        if cell != locked:
            count += 1
            locked = not locked

    return count


print(freed_prisoners([True, True, False, False, False, True, False]))
# ([True, True, False, False, False, True, False]) ➞ 4
#
# ([True, True, True]) ➞ 1
#
# ([False, False, False]) ➞ 0
#
# ([False, True, True, True]) ➞ 0