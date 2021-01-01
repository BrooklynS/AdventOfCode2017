import math

def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    jumplist = list(map(lambda line: int(line), lines))
    stepsTaken = 0
    index = 0
    while(index < len(jumplist)):
        stepsTaken += 1
        jump = jumplist[index]
        jumplist[index] += 1
        index += jump

    print(f'Part1: {stepsTaken}')

    jumplist = list(map(lambda line: int(line), lines))
    stepsTaken = 0
    index = 0
    while(index < len(jumplist)):
        stepsTaken += 1
        jump = jumplist[index]
        if(jumplist[index] >= 3):
            jumplist[index] -= 1
        else:
            jumplist[index] += 1
        index += jump

    print(f'Part2: {stepsTaken}')


def main():
    print("=========Test==========")
    runInput("inputs/problem05test.txt")
    print("=========Final==========")
    runInput("inputs/problem05input.txt")

if __name__ == '__main__':
    main()
