def win_round(your_cards, opponent_cards):
    your_number = int(''.join(map(str, sorted(your_cards, reverse=True)[:2])))
    opponent_number = int(''.join(map(str, sorted(opponent_cards, reverse=True)[:2])))
    return your_number > opponent_number


result = win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2])
print(result)
