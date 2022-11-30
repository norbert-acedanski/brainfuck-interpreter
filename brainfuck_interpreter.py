print_original_brainfuck_program = True
print_instructions_without_comments = True

program_filename = "brainfuck_program.txt"
BRAINFUCK_CHARACTERS = ['<', '>', '+', '-', '.', ',', '[', ']']
ARRAY_SIZE = 30000
brainfuck_array = bytearray(ARRAY_SIZE)


def load_program() -> str:
    try:
        with open(program_filename, "r", encoding="utf-8") as input_file:
            rough_program = input_file.readlines()
    except OSError:
        raise FileNotFoundError(f'File "{program_filename}" could not be opened. Check file name or file path.')
    joined_program = "".join(rough_program)
    return joined_program


def print_original_program(program: str):
    if print_original_brainfuck_program:
        print("\nOriginal program from the specified file:\n")
        print(program)
        print("")


def remove_redundant_characters(program: str) -> str:
    only_instruction_program = "".join([character for character in program if character in BRAINFUCK_CHARACTERS])
    return only_instruction_program


def print_only_instructions(program: str):
    if print_instructions_without_comments:
        print("\nInstructions from the specified file:\n")
        print(program)
        print("")


def make_bracket_list(program: str) -> list:
    bracket_list = [[], []] 
    number_of_opening_brackets = 0
    number_of_closing_brackets = 0
    for (index, instruction) in enumerate(program):
        if instruction == '[':
            number_of_opening_brackets += 1
            bracket_list[0].append(index)
            bracket_list[1].append(0)
        elif instruction == ']':
            number_of_closing_brackets += 1
            if number_of_closing_brackets > number_of_opening_brackets:
                raise SyntaxError(f"Mistake in the program. Found closing bracket without corresponding "
                                  f"opening bracket in position: {index}")
            for i in range(number_of_opening_brackets, 0, -1):
                if bracket_list[1][i - 1] == 0:
                    bracket_list[1][i - 1] = index
                    break
    if number_of_opening_brackets > number_of_closing_brackets:
        for i in range(number_of_opening_brackets):
            if bracket_list[1][i] == 0:
                raise SyntaxError(f"Mistake in the program. Found opening bracket without corresponding "
                                  f"closing bracket in position: {bracket_list[0][i]}")
    return bracket_list


def interpret_program(program: str, bracket_list: list):
    print("\nInterpreted program:\n")
    instruction_index = 0
    byte_array_index = 0
    while instruction_index != len(program):
        instruction = program[instruction_index]
        if   instruction == '<':
            byte_array_index = byte_array_index - 1 if byte_array_index > 0 else ARRAY_SIZE - 1
        elif instruction == '>':
            byte_array_index = byte_array_index + 1 if byte_array_index < ARRAY_SIZE - 1 else 0
        elif instruction == '+':
            brainfuck_array[byte_array_index] = brainfuck_array[byte_array_index] + 1 \
                if brainfuck_array[byte_array_index] < 255 else 0
        elif instruction == '-':
            brainfuck_array[byte_array_index] = brainfuck_array[byte_array_index] - 1 \
                if brainfuck_array[byte_array_index] > 0 else 255
        elif instruction == '.':
            print(chr(brainfuck_array[byte_array_index]), end="")
        elif instruction == ',':
            brainfuck_array[byte_array_index] = ord(input())
        elif instruction == '[':
            if brainfuck_array[byte_array_index] == 0:
                instruction_index = bracket_list[1][bracket_list[0].index(instruction_index)] + 1
                continue
        elif instruction == ']':
            instruction_index = bracket_list[0][bracket_list[1].index(instruction_index)]
            continue
        else:
            raise SyntaxError(f"Wrong input instruction at: {byte_array_index}")
        instruction_index += 1


if __name__ == '__main__':
    rough_program = load_program()
    print_original_program(rough_program)
    only_instruction_program = remove_redundant_characters(rough_program)
    print_only_instructions(only_instruction_program)
    bracket_list = make_bracket_list(only_instruction_program)
    interpret_program(only_instruction_program, bracket_list)