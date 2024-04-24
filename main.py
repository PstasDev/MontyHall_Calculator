import random

def monty_hall_simulation(num_simulations):
    stay_wins = 0
    switch_wins = 0
    num_doors = 3

    for simulation in range(1, num_simulations + 1):
        # Randomly place the car behind one of the doors
        doors = ['goat'] * num_doors
        car_position = random.randint(0, num_doors - 1)
        doors[car_position] = 'car'

        # Contestant makes an initial choice
        initial_choice = random.randint(0, num_doors - 1)

        # Monty opens a door with a goat behind it
        remaining_doors = [i for i in range(num_doors) if i != initial_choice and doors[i] == 'goat']
        monty_opens = random.choice(remaining_doors)

        # Contestant decides whether to stay or switch
        switch_choice = [i for i in range(num_doors) if i != initial_choice and i != monty_opens][0]

        # Check if contestant wins by staying
        if doors[initial_choice] == 'car':
            stay_wins += 1

        # Check if contestant wins by switching
        if doors[switch_choice] == 'car':
            switch_wins += 1

    stay_win_percentage = stay_wins / num_simulations * 100
    switch_win_percentage = switch_wins / num_simulations * 100

    print(f"Number of Simulations: {num_simulations}")
    print(f"Number of Doors: {num_doors}")
    print(f"Stay Wins: {stay_wins} ({stay_win_percentage:.2f}%)")
    print(f"Switch Wins: {switch_wins} ({switch_win_percentage:.2f}%)")

if __name__ == "__main__":
    num_simulations = 10000  # You can adjust the number of simulations
    monty_hall_simulation(num_simulations)
