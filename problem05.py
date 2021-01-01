import math
import time

def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    jumplist = list(map(lambda line: int(line), lines))
    stepsTaken = 0
    index = 0
    target = len(jumplist)
    while(index < target):
        stepsTaken += 1
        jump = jumplist[index]
        jumplist[index] += 1
        index += jump

    print(f'Part1: {stepsTaken}')

    jumplist = list(map(lambda line: int(line), lines))
    stepsTaken = 0
    index = 0
    target = len(jumplist)
    while(index < target):
        stepsTaken += 1
        jump = jumplist[index]
        if(jump >= 3):
            jumplist[index] -= 1
        else:
            jumplist[index] += 1

        index += jump

    print(f'Part2: {stepsTaken}')


def main():
    print("=========Test==========")
    time1 = time.perf_counter()
    runInput("inputs/problem05test.txt")
    time2 = time.perf_counter()
    print(f'Elapsed: {(time2 - time1)*1000:0.3f} ms')

    print("=========Final==========")
    time1 = time.perf_counter()
    runInput("inputs/problem05input.txt")
    time2 = time.perf_counter()
    print(f'Elapsed: {(time2 - time1)*1000:0.3f} ms')

if __name__ == '__main__':
    main()
