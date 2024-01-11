# ("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
# Examples
# ("--++--", "++--++") ➞ "000000"
#
# ("-+-+-+", "-+-+-+") ➞ "-+-+-+"
#
# ("-++-", "-+-+") ➞ "-+00"

def neutralise(s1, s2):
    res = ''
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            res += s1[i]
        if s1[1] == '+' and s2[i] == '-':
            res += '0'
        if s1[i] == '+' and s2[i] == '-':
            res += '+'
    return res

# I leveled up so time for 7-kyu // This was chalange number 20 not all are uploaded