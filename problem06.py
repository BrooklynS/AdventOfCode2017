import math

def hashBankList(items):
    sum = 0
    digit = 1

    for item in items:
        sum += item * digit
        digit *= 10
    
    return sum

def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    banklist = list(map(lambda line: int(line), lines[0].split()))
    bankhash = hashBankList(banklist)
    iterations = 0
    visited = {}
    while not bankhash in visited:
        
        iterations += 1
        visited[bankhash] = iterations

        itemsToDistribute = max(banklist)
        redistributionIndex = banklist.index(itemsToDistribute)
        banklist[redistributionIndex] = 0
        
        while itemsToDistribute > 0:
            redistributionIndex += 1
            redistributionIndex %= len(banklist)

            banklist[redistributionIndex] += 1
            itemsToDistribute -= 1
        
        bankhash = hashBankList(banklist)

    
    print(f'Part1: {iterations}')
    print(f'Part2: {iterations + 1 - visited[bankhash]}')


def main():
    print("=========Test==========")
    runInput("inputs/problem06test.txt")
    print("=========Final==========")
    runInput("inputs/problem06input.txt")

if __name__ == '__main__':
    main()
