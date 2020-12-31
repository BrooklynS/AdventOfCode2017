import math

def part1ValidPassword(password : str):

    words = password.split()
    existing = set(words)
    return len(existing) == len(words)

def part2ValidPassword(password : str):

    words = password.split()
    sortedSet = set()
    for word in words:
        sortedSet.add("".join(sorted(word)))
    
    return len(sortedSet) == len(words) 


def runInput(filename : str):
    
    with open(filename, "r") as file:
        lines = file.readlines()
    
    validPasswords = 0
    validPasswords2 = 0
    for password in lines:
        if(part1ValidPassword(password)):
            validPasswords += 1
        if(part2ValidPassword(password)):
            validPasswords2 += 1
    
    print(f'Part1: {validPasswords}')
    print(f'Part2: {validPasswords2}')


def main():
    print("=========Test==========")
    runInput("inputs/problem04test.txt")
    print("=========Final==========")
    runInput("inputs/problem04input.txt")

if __name__ == '__main__':
    main()
