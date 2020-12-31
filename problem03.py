import math


def spiral_iterator() -> tuple[int, int]:

    yield (0, 0)

    xloc = 0
    yloc = 0
    iteration = 0
    while True:
        iteration += 1
        sideelements = iteration * 2
        xloc = iteration
        yloc = iteration
        # rightside
        for __ in range(0, sideelements):
            yloc -= 1
            yield(xloc, yloc)
        # top
        for __ in range(0, sideelements):
            xloc -= 1
            yield(xloc, yloc)
        #left
        for __ in range(0, sideelements):
            yloc += 1
            yield(xloc, yloc)
        # bottom
        for __ in range(0, sideelements):
            xloc += 1
            yield(xloc, yloc)


def part1(targetValue : int):
    
    iterator = spiral_iterator()
    for __ in range(0, targetValue):
        item = next(iterator) 

    return abs(item[0]) + abs(item[1])


def part2(targetValue : int):
    
    cache = {
        (0,0): 1
    }

    diagonalOffsets = []
    for xoffset in range(-1, 2):
        for yoffset in range(-1, 2):
            if(xoffset != 0 or yoffset != 0):
                diagonalOffsets.append([xoffset, yoffset])

    iterator = spiral_iterator()
    # skip first location.
    next(iterator)
    for item in iterator:

        sum = 0
        for offset in diagonalOffsets:
            neighbor = (item[0] + offset[0], item[1] + offset[1])
            if neighbor in cache:
                sum += cache[neighbor]
        
        cache[item] = sum

        if(sum > targetValue):
            return sum


def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    target = int(lines[0])
    print(f'Part1: {part1(target)}')
    print(f'Part2: {part2(target)}')


def main():
    print("=========Test==========")
    runInput("inputs/problem03test.txt")
    print("=========Final==========")
    runInput("inputs/problem03input.txt")

if __name__ == '__main__':
    main()
