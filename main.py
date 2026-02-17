# Create 3x3 grid with empty spaces
grid = [[" " for _ in range(3)] for _ in range(3)]


def print_board():
    print("\n")
    for i in range(3):
        # Print row with cells
        print(" " + grid[i][0] + " | " + grid[i][1] + " | " + grid[i][2])

        # Print separator line (except after last row)
        if i < 2:
            print("-----------")
    print("\n")


def get_grid_pos(pos):
    pos = int(pos) - 1
    row = pos // 3
    col = pos % 3
    return row, col


def select_player():
    while True:
        player1 = input("Select Player (X or O): ").upper().strip()

        if player1 in ["X", "O"]:
            if player1 == "X":
                opponent = "O"
            else:
                opponent = "X"
            return player1, opponent
        else:
            print("Invalid! Enter a valid player")


def game(player):
    while True:
        choice = input("Enter the position for your play (1-9): ").strip()
        if not choice.isdigit():
            print("Invalid! Enter a valid digit")
            continue

        pos = int(choice)
        if pos not in range(1, 10):
            print("Invalid! Enter a valid posision")
            continue

        row, col = get_grid_pos(pos)
        if grid[row][col] != " ":
            print("Invalid! Your opponent has already filled that box")
            continue

        grid[row][col] = player
        print_board()
        break


winning_lines = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],  # Three rows
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],  # Three columns
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],  # Two diagonals
]

all_positions = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
]


def reset_board():
    for i in winning_lines:
        grid[i[0][0]][i[0][1]] = " "
        grid[i[1][0]][i[1][1]] = " "
        grid[i[2][0]][i[2][1]] = " "

    print_board()


def check_winner():
    for line in winning_lines:
        pos1 = grid[line[0][0]][line[0][1]]
        pos2 = grid[line[1][0]][line[1][1]]
        pos3 = grid[line[2][0]][line[2][1]]

        if pos1 == pos2 == pos3 and pos1 != " ":
            return pos1

    return False


def is_draw():
    for pos in all_positions:
        if grid[pos[0]][pos[1]] == " ":
            return False
    return True


def main():
    while True:
        reset_board()
        you, opponent = select_player()
        turn_player1 = True
        while True:
            if turn_player1:
                game(you)
                turn_player1 = False
            else:
                game(opponent)
                turn_player1 = True

            winner = check_winner()
            if winner:
                if winner == you:
                    print("You are the winner")

                elif winner == opponent:
                    print("Your opponent won the game")
                break
            elif is_draw():
                print("It's a Draw")
                break

            print("Opponent's Turn" if turn_player1 == False else "Your Turn")

        again = input("Wanna play again? (y/n): ").lower()
        if again != "y":
            print("Game over")
            break


if __name__ == "__main__":
    main()
