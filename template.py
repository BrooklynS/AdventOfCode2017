import os, sys, pathlib

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        raise "Please specify a name, e.g. problem01"
    
    with open("template.txt", "r") as file:
        lines = file.readlines()
    
    output = []
    for line in lines:
        output.append(line.replace("##PROBLEMNAME##", args[1]))
    
    pyFilename = args[1] + ".py"
    testFilename = "inputs/" + args[1] + "test.txt"
    inputFileName = "inputs/" + args[1] + "input.txt"
    cwd = pathlib.Path.cwd()

    with open(pyFilename, "w+") as file:
        file.writelines(output)
        file.close()

    with open(testFilename, "w+") as file:
        file.write("")
        file.close()

    with open(inputFileName, "w+") as file:
        file.write("")
        file.close()

    os.startfile(cwd.joinpath(testFilename).resolve())
    os.startfile(cwd.joinpath(inputFileName).resolve())
    os.startfile(cwd.joinpath(pyFilename).resolve())

