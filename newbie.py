from sly import Lexer

class MyLexer(Lexer):

    tokens = {ASSIGN, INT, FLOAT, BOOLEAN, STRING, CHAR, VALUE}

    ASSIGN = '='
    INT = r'^int'
    FLOAT = r'^float'
    BOOLEAN = r'^boolean'
    STRING = r'^string'
    CHAR = r'^char'
    VALUE = r'[a-zA-Z0-9]*'
    # IGNORED = ' \t'

if __name__ == '__main__':
    data = ('int m = 10')
    lexer = MyLexer()

    for token in lexer.tokenize(data):
        print(token)

