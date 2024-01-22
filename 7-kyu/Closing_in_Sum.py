def closing_in_sum(n):
    number_str = str(n)
    length = len(number_str)

    sum_result = 0
    for i in range(length // 2):
        first_digit = int(number_str[i])
        last_digit = int(number_str[length - 1 - i])
        formed_number = int(str(first_digit) + str(last_digit))
        sum_result += formed_number

    if length % 2 == 1:
        sum_result += int(number_str[length // 2])

    return sum_result


print(closing_in_sum(121))