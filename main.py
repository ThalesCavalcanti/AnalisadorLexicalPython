from analisador_lexical import Lexer, LexicalError

src = "int y = @123\nprint(x + .5)\n#comentario de linha\n/*comentario de bloco*/"
lex = Lexer(src)
tokens = lex.tokenize()
for t in tokens:
    print(t)
