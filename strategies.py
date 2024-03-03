import random

def martingale(initial_bet, num_losses):
    total_bet = initial_bet * (2 ** num_losses)
    return total_bet

def anti_martingale(initial_bet, num_wins):
    total_bet = initial_bet * (2 ** num_wins)
    return total_bet

def labouchere(starting_sequence, current_sequence):
    bet = starting_sequence[0] + starting_sequence[-1]
    return bet, current_sequence[1:-1]

def fibonacci(starting_sequence, current_sequence):
    bet = starting_sequence[0]
    return bet, (current_sequence[1:] if len(current_sequence) > 1 else [])

def dalembert(initial_bet, num_losses, num_wins):
    bet = initial_bet + num_losses - num_wins
    return bet

def double_on_loss(initial_bet, num_losses):
    bet = initial_bet * (2 ** num_losses)
    return bet

def one_three_two_six(initial_bet, sequence):
    bet = sequence[0]
    return bet, sequence[1:] if len(sequence) > 1 else []
