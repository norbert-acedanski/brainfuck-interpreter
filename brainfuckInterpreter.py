import sys

printOriginalBrainFuckProgram = True
printInstructionsWithouComment = True

programName = "brainFuckProgram.txt"
brainFuckCharacters = ['<', '>', '+', '-', '.', ',', '[', ']']
ARRAY_SIZE = 30000
brainFuckArray = bytearray(ARRAY_SIZE)

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
    byteArrayIndex = 0
    for instruction in program:
        if   instruction == '<':
            byteArrayIndex = byteArrayIndex - 1 if byteArrayIndex > 0 else ARRAY_SIZE - 1
        elif instruction == '>':
            byteArrayIndex = byteArrayIndex + 1 if byteArrayIndex < ARRAY_SIZE - 1 else 0
        elif instruction == '+':
            brainFuckArray[byteArrayIndex] = brainFuckArray[byteArrayIndex] + 1 if brainFuckArray[byteArrayIndex] < 255 else 0
        elif instruction == '-':
            brainFuckArray[byteArrayIndex] = brainFuckArray[byteArrayIndex] - 1 if brainFuckArray[byteArrayIndex] > 0 else 255
        elif instruction == '.':
            print(chr(brainFuckArray[byteArrayIndex]))
        elif instruction == ',':
            brainFuckArray[byteArrayIndex] = ord(input())
        elif instruction == '[':
            pass
        elif instruction == ']':
            pass
        else:
            print("Wrong input instruction at: " + str(byteArrayIndex))
            sys.exit()

if __name__ == '__main__':
    roughProgram = loadProgram()
    printOriginalProgram(roughProgram)
    onlyInstructionProgram = removeRedundantCharacters(roughProgram)
    printOnlyInstructions(onlyInstructionProgram)
    interpretProgram(onlyInstructionProgram)