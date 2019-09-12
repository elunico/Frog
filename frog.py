import random
import sys
import shutil
import os

ROUNDS = 1000000


def get_terminal_rows_cols():
    first = shutil.get_terminal_size((0, 0))
    if first.columns == 0:
        second = os.popen('stty size', 'r').read().split()
        try:
            rows, cols = int(second[0]), int(second[1])
            return rows, cols
        except (TypeError, ValueError):
            raise ValueError("Could not find terminal size")
    else:
        return first.lines, first.columns


_, COLS = get_terminal_rows_cols()


def main():
    steps = 0
    for i in range(ROUNDS):
        if i % (ROUNDS/100) == 0:
            show_status(i, ROUNDS)
        spots = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # start at -1
        next_spot = -1
        while next_spot != 9:
            next_spot = random.choice(spots)
            spots = spots[spots.index(next_spot) + 1:]
            steps += 1
        assert next_spot == 9 and spots == [], 'Illegal State: did not end on last spot'

    show_status(1, 1)
    print('')
    print("Average number of steps is {}".format(steps / ROUNDS))


def show_status(round, rounds):
    msg = 'running simulation: {:03.0f}% '.format((round / rounds) * 100)
    bar = '#' * int((round/rounds) * (COLS - len(msg)))
    print(msg, end='')
    print(bar, end='')
    print('\x08' * (len(msg) + len(bar)), end='')
    sys.stdout.flush()


if __name__ == "__main__":
    ROUNDS = int(sys.argv[1])
    main()
