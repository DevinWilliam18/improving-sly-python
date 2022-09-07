from multiprocessing.sharedctypes import Value
from sly import Lexer

class CobaLexer(Lexer):
    tokens = {IF, THEN, VALUE}
    ignore = ' \n'
    IF = r"(?i)JIKA"
    THEN = r"(?i)MAKA"
    VALUE = r"[a-zA-Z][a-zA-Z0-9]*"

if __name__ == '__main__':
    data = "Jika hari ini training maka senang"
    lexer = CobaLexer()

    for token in lexer.tokenize(data):
        print(token)