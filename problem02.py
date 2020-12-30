import math


def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    sum = 0
    for line in lines:
        nums = [int(numstring) for numstring in line.split()]
        sum += max(nums) - min(nums)
    
    print("Part1: " + str(sum))

    sum = 0
    for line in lines:
        nums = [int(numstring) for numstring in line.split()]
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                first = nums[i]
                second = nums[j]
                if(j != i and second != 0):
                    if(first % second == 0):
                        sum += int(first / second)
    
    print("Part2: " + str(sum))


def main():
    print("=========Test==========")
    runInput("inputs/problem02test.txt")
    print("=========Final==========")
    runInput("inputs/problem02input.txt")

if __name__ == '__main__':
    main()
