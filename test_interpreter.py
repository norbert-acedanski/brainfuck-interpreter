from ast import In
import pytest

from brainfuck_interpreter import *

VALID_PROGRAM = "[,.[.],..,,,+,-,<>,[]..]++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
INVALID_PROGRAM_1 = ",.[.],..,,,+,-,<>,[]..]++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
INVALID_PROGRAM_2 = "[,.[.],..,,,+,-,<>,[]..++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
INVALID_PROGRAM_3 = "[,.[.],..,,,+,-,<>,[]..]++++++++[>++++[>++>+++>+++>+<<<<->+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
INVALID_PROGRAM_4 = "[,.[.],..,,,+,-,<>,[]..]++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

@pytest.mark.parametrize("program", [INVALID_PROGRAM_1, INVALID_PROGRAM_2, INVALID_PROGRAM_3, INVALID_PROGRAM_4])
def test_interpreter_edge_case(program):
    with pytest.raises(SyntaxError):
        make_bracket_list(program)

def test_interpreter(capsys):
    bracket_list = make_bracket_list(VALID_PROGRAM)
    interpret_program(VALID_PROGRAM, bracket_list)
    captured_print = capsys.readouterr()
    assert "Hello World!" in captured_print.out