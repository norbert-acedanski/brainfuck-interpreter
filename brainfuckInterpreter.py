import sys

printOriginalBrainFuckProgram = True
printInstructionsWithouComment = True

programName = "brainFuckProgram.txt"
brainFuckCharacters = ['<', '>', '+', '-', '.', ',', '[', ']']
ARRAY_SIZE = 30000
brainFuckArray = bytearray(ARRAY_SIZE)
bracketDictionary = {}

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

def makeBracketDictionary(program):
    numberOfOpeningBrackets = 0
    numberOfClosingBrackets = 0
    for (index, instruction) in enumerate(program):
        if instruction == '[':
            numberOfOpeningBrackets += 1
            bracketDictionary[str(numberOfOpeningBrackets - 1)] = [index, 0]
        elif instruction == ']':
            numberOfClosingBrackets += 1
            if numberOfClosingBrackets > numberOfOpeningBrackets:
                print("Mistake in the program. Found closing bracket without corresponding opening bracket in position: " + str(index))
                sys.exit()
            for i in range(numberOfOpeningBrackets, 0, -1):
                if bracketDictionary[str(i - 1)][1] == 0:
                    bracketDictionary[str(i - 1)][1] = index
                    break
    if numberOfOpeningBrackets > numberOfClosingBrackets:
        for i in range(numberOfOpeningBrackets):
            if bracketDictionary[str(i)][1] == 0:
                print("Mistake in the program. Found opening bracket without corresponding closing bracket in position: " + str(bracketDictionary[str(i)][0]))
                sys.exit()

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
    makeBracketDictionary(onlyInstructionProgram)
    interpretProgram(onlyInstructionProgram)