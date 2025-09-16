from analisador_lexical import Lexer, LexicalError

src = "int y = 123+321*2/4-6 \n x>y != x<y == x<=y >= y \n a(b) = 1.5 + 2.0 \n print if else float int \n #comentario de linha unica \n /* comentario de \n multiplas linhas */ "
src_erro = "@123"
lex = Lexer(src)
tokens = lex.tokenize()
for t in tokens:
    print(t)
