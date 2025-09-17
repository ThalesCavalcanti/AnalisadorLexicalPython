from analisador_lexical import Lexer, LexicalError

def main():
    filename = "programa.mc"  # Change to your .mc file name
    try:
        with open(filename, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
        return

    lex = Lexer(src)
    try:
        tokens = lex.tokenize()
        for t in tokens:
            print(t)
    except LexicalError as e:
        print(f"Erro léxico: {e}")

if __name__ == "__main__":
    main()
