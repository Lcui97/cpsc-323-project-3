from tools.lexer.lexer_main import lexer
from tools.parser.parser_main import parser

def main():
    token_stream = lexer("./test_cases/1.in")

    # Test
    parser_input = ' '.join(token_stream)
    with open('foo.in', 'w') as file:
        file.write(parser_input)
    # Change this function below to accept not from .in file but directly from token_stream (array)
    parser("./foo.in")

if __name__ == "__main__":
    main()