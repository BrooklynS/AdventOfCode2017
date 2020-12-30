import math

def getCircularMatchingSum(input : str, circularOffset : int) -> int:
    
    sum = 0
    for index in range(0, len(input)):
        offset = (index + circularOffset) % len(input)
        if(input[index] == input[offset]):
            sum += int(input[index])

    return sum
    

def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    print("Part1: " + str(getCircularMatchingSum(lines[0], 1)))
    halfOffset = math.floor(len(lines[0]) / 2)
    print("Part2: " + str(getCircularMatchingSum(lines[0], halfOffset)))


def main():
    print("=========Test==========")
    runInput("inputs/problem01test.txt")
    print("=========Final==========")
    runInput("inputs/problem01input.txt")

if __name__ == '__main__':
    main()
