#!/usr/bin/python3
'''0-prime_game.py'''


def is_prime(num):
    ''' function that find the prime number'''
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    '''Function that retreive the winner'''
    if x < 1 or not nums:
        return None

    marias_wins = sum(1 for n in nums if is_prime(n) and n % 2 == 1)
    bens_wins = sum(1 for n in nums if is_prime(n) and n % 2 == 0)

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
