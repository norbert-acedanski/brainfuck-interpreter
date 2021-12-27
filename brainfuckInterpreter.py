printOriginalBrainFuckProgram = True
printInstructionsWithouComment = True

programName = "brainFuckProgram.txt"
brainFuckCharacters = ['<', '>', '+', '-', '.', ',', '[', ']']
brainFuckArray = bytearray(30000)

def loadProgram():
    with open(programName, "r", encoding="utf-8") as inputFile:
        roughProgram = inputFile.readlines()
    joinedProgram = "".join(roughProgram)
    return joinedProgram

def printOriginalProgram(program):
    if printOriginalBrainFuckProgram:
        print("Original program from the specified file:\n")
        print(program)
        print("")

def removeRedundantCharacters(program):
    onlyInstructionList = [character for character in program if character in brainFuckCharacters]
    onlyInstructionProgram = "".join(onlyInstructionList)
    return onlyInstructionProgram

def printOnlyInstructions(program):
    if printInstructionsWithouComment:
        print("Instructions from the specified file:\n")
        print(program)
        print("")

def interpretProgram(program):
    pass

if __name__ == '__main__':
    roughProgram = loadProgram()
    printOriginalProgram(roughProgram)
    onlyInstructionProgram = removeRedundantCharacters(roughProgram)
    printOnlyInstructions(onlyInstructionProgram)
    interpretProgram(onlyInstructionProgram)