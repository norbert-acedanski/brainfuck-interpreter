import sys

printOriginalBrainFuckProgram = True
printInstructionsWithoutComment = True

programName = "brainFuckProgram.txt"
brainFuckCharacters = ['<', '>', '+', '-', '.', ',', '[', ']']
ARRAY_SIZE = 30000
brainFuckArray = bytearray(ARRAY_SIZE)
bracketList = [[], []]

def loadProgram():
    with open(programName, "r", encoding="utf-8") as inputFile:
        roughProgram = inputFile.readlines()
    joinedProgram = "".join(roughProgram)
    return joinedProgram

def printOriginalProgram(program):
    if printOriginalBrainFuckProgram:
        print("\nOriginal program from the specified file:\n")
        print(program)
        print("")

def removeRedundantCharacters(program):
    onlyInstructionList = [character for character in program if character in brainFuckCharacters]
    onlyInstructionProgram = "".join(onlyInstructionList)
    return onlyInstructionProgram

def printOnlyInstructions(program):
    if printInstructionsWithoutComment:
        print("\nInstructions from the specified file:\n")
        print(program)
        print("")

def makeBracketDictionary(program):
    numberOfOpeningBrackets = 0
    numberOfClosingBrackets = 0
    for (index, instruction) in enumerate(program):
        if instruction == '[':
            numberOfOpeningBrackets += 1
            bracketList[0].append(index)
            bracketList[1].append(0)
        elif instruction == ']':
            numberOfClosingBrackets += 1
            if numberOfClosingBrackets > numberOfOpeningBrackets:
                print("Mistake in the program. Found closing bracket without corresponding opening bracket in position: " + str(index))
                sys.exit()
            for i in range(numberOfOpeningBrackets, 0, -1):
                if bracketList[1][i - 1] == 0:
                    bracketList[1][i - 1] = index
                    break
    if numberOfOpeningBrackets > numberOfClosingBrackets:
        for i in range(numberOfOpeningBrackets):
            if bracketList[i][1] == 0:
                print("Mistake in the program. Found opening bracket without corresponding closing bracket in position: " + str(bracketList[i][0]))
                sys.exit()

def interpretProgram(program):
    print("\nInterpreted program:\n")
    instructionIndex = 0
    byteArrayIndex = 0
    while instructionIndex != len(program):
        instruction = program[instructionIndex]
        if   instruction == '<':
            byteArrayIndex = byteArrayIndex - 1 if byteArrayIndex > 0 else ARRAY_SIZE - 1
        elif instruction == '>':
            byteArrayIndex = byteArrayIndex + 1 if byteArrayIndex < ARRAY_SIZE - 1 else 0
        elif instruction == '+':
            brainFuckArray[byteArrayIndex] = brainFuckArray[byteArrayIndex] + 1 if brainFuckArray[byteArrayIndex] < 255 else 0
        elif instruction == '-':
            brainFuckArray[byteArrayIndex] = brainFuckArray[byteArrayIndex] - 1 if brainFuckArray[byteArrayIndex] > 0 else 255
        elif instruction == '.':
            print(chr(brainFuckArray[byteArrayIndex]), end="")
        elif instruction == ',':
            brainFuckArray[byteArrayIndex] = ord(input())
        elif instruction == '[':
            if brainFuckArray[byteArrayIndex] == 0:
                instructionIndex = bracketList[1][bracketList[0].index(instructionIndex)] + 1
                continue
        elif instruction == ']':
            instructionIndex = bracketList[0][bracketList[1].index(instructionIndex)]
            continue
        else:
            print("Wrong input instruction at: " + str(byteArrayIndex))
            sys.exit()
        instructionIndex += 1

if __name__ == '__main__':
    roughProgram = loadProgram()
    printOriginalProgram(roughProgram)
    onlyInstructionProgram = removeRedundantCharacters(roughProgram)
    printOnlyInstructions(onlyInstructionProgram)
    makeBracketDictionary(onlyInstructionProgram)
    interpretProgram(onlyInstructionProgram)