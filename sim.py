
import random
from strategies import martingale, anti_martingale, labouchere, fibonacci, dalembert, double_on_loss, one_three_two_six

def simulate_strategy(strategy_function, num_rounds, win_probability):
    total_profit = 0
    current_bet = 5  # Initial bet size (adjust as needed)

    for _ in range(num_rounds):
        if random.random() < win_probability:  # Simulating a win
            total_profit += current_bet
            current_bet = 5  # Reset bet size after a win
        else:  # Simulating a loss
            total_profit -= current_bet
            current_bet = strategy_function(current_bet)  # Adjust bet size based on strategy

    return total_profit

# Parameters
num_rounds = 1000
win_probability = 0.5  # Assuming a 50% chance of winning

# Simulate each strategy
strategies = [martingale, anti_martingale, labouchere, fibonacci, dalembert, double_on_loss, one_three_two_six]

for strategy in strategies:
    total_profit = simulate_strategy(strategy, num_rounds, win_probability)
    print(f"{strategy.__name__}: Total Profit after {num_rounds} rounds: ${total_profit}")
