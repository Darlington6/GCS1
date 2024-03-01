def get_valid_odd_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num % 2 == 1 and num > 0:
                return num
            else:
                print("Please enter a positive odd number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_player_names():
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    return player1, player2

def main():
    num_stones = get_valid_odd_number("Enter the starting number of stones: ")
    player1, player2 = get_player_names()

    stones_left = num_stones
    player1_stones = 0
    player2_stones = 0

    while stones_left > 0:
        print(f"\nStones left: {stones_left}")

        # Player 1's turn
        choice = int(input(f"{player1}, choose between 1 and {stones_left // 2}: "))
        while choice <= 0 or choice > stones_left // 2:
            print("Invalid amount. Please choose a valid number of stones.")
            choice = int(input(f"{player1}, choose between 1 and {stones_left // 2}: "))
        player1_stones += choice
        stones_left -= choice
        print(f"{player1} now has {player1_stones} stones.")

        if stones_left == 0:
            break

        # Player 2's turn
        choice = int(input(f"{player2}, choose between 1 and {min(2 * choice, stones_left)}: "))
        while choice <= 0 or choice > min(2 * player1_stones, stones_left):
            print("Invalid amount. Please choose a valid number of stones.")
            choice = int(input(f"{player2}, choose between 1 and {min(2 * choice, stones_left)}: "))
        player2_stones += choice
        stones_left -= choice
        print(f"{player2} now has {player2_stones} stones.")

    if player1_stones % 2 == 1:
        print(f"\n{player1} wins!")
    else:
        print(f"\n{player2} wins!")

if __name__ == "__main__":
    main()
