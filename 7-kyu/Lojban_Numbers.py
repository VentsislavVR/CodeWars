def convert_lojban(lojban):
    mapper = {
        1: 'pa', 4: 'vo', 7: 'ze',
        2: 're', 5: 'mu', 8: 'bi', 0: 'no',
        3: 'ci', 6: 'xa', 9: 'so',
    }
    result_str = ""
    for index in range(0, len(lojban), 2):
        current_pair = lojban[index:index + 2]
        if current_pair in mapper.values():
            key = next(key for key, value in mapper.items() if value == current_pair)
            result_str += str(key)

    return int(result_str)

result = convert_lojban('renonore')
print(result)
