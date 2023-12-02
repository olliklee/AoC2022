#  Solutions of Advent of Code
#  Oliver Kleemann

from time import perf_counter

year, day = "2022", "01"


def run(d, y):
    print(f"\nResults from AoC {y} - Day {d}\n{'-' * 30}")

    start = perf_counter()
    print(f"Day {d} - Part 1: {solve_a()}")

    lap = perf_counter()
    print(f"Day {d} - Part 2: {solve_b()}")

    stop = perf_counter()

    print(f"\nPerformance\n{'-' * 30}")
    print(f"Part 1: {(lap - start) * 100:.6f} ms\nPart 2: {(stop - lap)*100:.6f} ms")
    print(f"{'-' * 30}\nGesamt: {(stop - start)*100:.6f} ms")


def prepare_input(file_name):
    with open(file_name) as f:
        calories = []
        for line in f:
            line = line.strip()
            calories.append(line)
    # sum up calories for each elv
    sumup = 0
    elves = []
    for num in calories:
        if num != "":
            sumup += int(num)
        else:
            elves.append(sumup)
            sumup = 0

    elves.sort(reverse=True)
    return elves


def solve_a():
    elves_inventory = prepare_input("Day01_input.txt")
    # winner is:
    return elves_inventory[0]


def solve_b():
    elves_inventory = prepare_input("Day01_input.txt")
    # top 3 are:
    return sum(elves_inventory[:3])


run(day, year)
