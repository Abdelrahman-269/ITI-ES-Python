from typing import NamedTuple
import re


class Token(NamedTuple):
    # If u don't know what a class is think of this as a struct with 4 variables inside it.
    type: str
    value: str
    line: int
    column: int


def tokenize(code):
    # ToDo:add the rest of the keywords;
    keywords_cpp = {'auto', 'break', 'case', 'char',
                    'const', 'continue', 'default', 'do',
                    'double', 'else', 'enum', 'extern',
                    'float', 'for', 'goto', 'if',
                    'int', 'long', 'register', 'return',
                    'short', 'signed', 'sizeof', 'static',
                    'struct', 'switch', 'typedef', 'union',
                    'unsigned', 'void', 'volatile', 'while',
                    'asm', 'dynamic_cast', 'explicit', 'operator',
                    'this', 'delete', 'new', 'static_cast', 'false',
                    'catch', 'namespace', 'reinterpret_cast', 'bool',
                    'template', 'friend', 'private', 'class', 'inline',
                    'public', 'throw', 'const_cast', 'mutable', 'typeid',
                    'protected', 'true', 'try', 'typename',
                    'using', 'virtual', 'wchar_t'}
    # each element in the token_specification list is a named tuple that represents a possible token
    token_specification = [
        # ToDo: Check this example then complete the rest of the tokens.
        # I use a namedtuple in here. It's like a normal tuple but with named fields.
        # So i can get the values using names.
        ('block_comment', r'\/\*[a-zA-Z_0-9]*\*\/$'),
		('line_comment', r'\/\/.*'),
		('assignment_operator', r'=|(/=)|\*=|%=|\+=|-=|>>=|<<=|&=|^=|\|='),  # assignment-operator identifier
        ('identifier', r'[a-zA-Z_][a-zA-Z_0-9]+'),
        ('letter_', r'[a-zA-Z_]'),
		('digits', r'[0-9]+'),       
	    ('digit', r'[0-9]'),
        ('relational_operator', r'<|>|>=|<=|==|\!='),
        ('logical_operator', r'(\|\|)|(\&\&)|\!'),
		
		  
		('unary_operator', r'\*|\&|\+|\-|\!|\~')
		

    ]

    # This creates a regular expression that contains all the expressions u wrote in the token_specification list.
    # it uses the property that the regular expression a|b will get either a or b .
    # The syntax uses an idea called list comprehension to create a one line code.
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)


    line_num = 1
    line_start = 0
    # This for loop iterates over all the found matches in the input code and then creates a token for each match.
    # The finditer method can be found in the python documentation linked in the Task page.
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        # These lines give an example on some processing done to found tokens.
        # U can ignore them if u want.

        # if kind == 'NUMBER':
        #     value = float(value) if '.' in value else int(value)
        # elif kind == 'ID' and value in keywords_cpp:
        #     kind = value
        # elif kind == 'NEWLINE':
        #     line_start = mo.end()
        #     line_num += 1
        #     continue
        # elif kind == 'SKIP':
        #     continue
        # elif kind == 'MISMATCH':
        #     raise RuntimeError(f'{value!r} unexpected on line {line_num}')

        # The yield statement is part f a concept called generators in python.
        yield Token(kind, value, line_num, column)


statements = '= /= *= %= += -= >>= <<= &= ^= |= (&&) ! (23df) /*dds45sadd*/ auto /*sagdsfx*/'

# ToDo: U have to add the file handling logic in here and then pass the code to the tokenize() function.
for token in tokenize(statements):
    print(token)

# if __name__ == '__main__':
#   main()
