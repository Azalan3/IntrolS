from typing import List


def get_rounds(number: int) -> List[int]:
    """Devuelve [round_actual, siguiente, siguiente_del_siguiente]."""
    return [number, number + 1, number + 2]

print(get_rounds(27))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """Concatena dos listas de rondas."""
    return rounds_1 + rounds_2

print(concatenate_rounds([27, 28, 29], [35, 36]))


def list_contains_round(rounds: List[int], round_number: int) -> bool:
    """Indica si round_number está en rounds."""
    return round_number in rounds

print(list_contains_round([27, 28, 29, 35, 36], 29))  
print(list_contains_round([27, 28, 39, 35, 36], 30))


def card_average(hand: List[int]) -> float:
    """Promedio (media aritmética) de los valores de la mano."""
    return sum(hand) / len(hand)

print(card_average([5, 6, 7]))


def approx_average_is_average(hand: List[int]) -> bool:
    """Comprueba si alguna aproximación (extremos/2 o carta del medio) iguala la media real."""
    real_average = card_average(hand)
    approx_1 = (hand[0] + hand[-1]) / 2
    approx_2 = hand[len(hand) // 2]
    return real_average in (approx_1, approx_2)

print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))


def average_even_is_average_odd(hand: List[int]) -> bool:
    """Compara la media de índices pares vs impares."""
    even_cards = hand[0::2]
    odd_cards = hand[1::2]
    return card_average(even_cards) == card_average(odd_cards)

print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))


def maybe_double_last(hand: List[int]) -> List[int]:
    """Si la última carta es J (11), duplica su valor y devuelve una copia de la mano."""
    new_hand = hand[:]  # copia (no muta la original)
    if new_hand and new_hand[-1] == 11:
        new_hand[-1] *= 2
    return new_hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))
