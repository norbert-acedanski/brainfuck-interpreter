
programName = "brainFuckProgram.txt"
brainFuckCharacters = ['<', '>', '+', '-', '.', ',', '[', ']']

def loadProgram():
    with open(programName, "r", encoding="utf-8") as inputFile:
        roughProgram = inputFile.readlines()
    joinedProgram = "".join(roughProgram)
    return joinedProgram

def removeRedundantCharacters(program):
    onlyInstructionList = [character for character in program if character in brainFuckCharacters]
    onlyInstructionProgram = "".join(onlyInstructionList)
    return onlyInstructionProgram

if __name__ == '__main__':
    roughProgram = loadProgram()
    onlyInstructionProgram = removeRedundantCharacters(roughProgram)
    print(onlyInstructionProgram)