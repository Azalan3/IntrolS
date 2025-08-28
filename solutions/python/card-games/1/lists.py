def get_rounds(number):
    numer = int(number)
    return [number, number + 1, number + 2]
print(get_rounds(27))

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2
print(concatenate_rounds([27, 28, 29], [35, 36]))

def list_contains_round(rounds, round_number):
    if round_number in rounds:
        return True
    else:
        return False
print(list_contains_round([27, 28, 29, 35, 36], 29))  
print(list_contains_round([27, 28, 39, 35, 36], 30))

def card_average(hand):
    return sum(hand) / len(hand)
print(card_average([5, 6, 7]))

def approx_average_is_average(hand):

    Real_average = card_average(hand)

    Aprox_1 = (hand[0]+ hand[-1]) / 2
    Aprox_2 = hand[len(hand) // 2]

    if Real_average == Aprox_1 or Real_average == Aprox_2:
        return True
    else:
        return False


print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))

def average_even_is_average_odd(hand):

    average_even = (sum(hand[0::2]) / len(hand[0::2]))
    average_odd = (sum(hand[1::2]) / len(hand[1::2]))
    if average_even == average_odd:
        return True
    else:
        return False


print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))

def maybe_double_last(hand):

    hand_original = hand[:]
    
    if hand[-1] == 11:
        hand_original[-1] = hand[-1] * 2
    return hand_original
print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10])) 