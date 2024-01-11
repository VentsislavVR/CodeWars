def spin_around(lst):
    total = 0
    left = lst.count('left')
    right = lst.count('right')

    if left == right:
        return total
    elif left > right:
        total = left - right
        return total // 4
    else:
        total = right - left
        return total // 4


"""
Given a list of directions to spin, "left" or "right",
 return an integer of how many full 360° rotations were made. 
 Note that each word in the array counts as a 90° rotation in that direction.

Worked Example
["right", "right", "right", "right", "left", "right"] ➞ 1
# You spun right 4 times (90 * 4 = 360)
# You spun left once (360 - 90 = 270)
# But you spun right once more to make a full rotation (270 + 90 = 360)
"""

print(spin_around(["left", "right", "left", "right"]))

print(spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]))
print(spin_around(["left", "left", "left", "left"]))
