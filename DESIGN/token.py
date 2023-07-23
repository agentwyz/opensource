class Token:
    #常见的token表示
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"
    NEGATE = "NEGATE"
    COMMUTE = "COMMUTE"
    LPARENS = "LPARENS"
    RPARENS = "RPARENS"
    EOF = "EOF"

    FUNCTIONS = [PLUS, MINUS, TIMES, DIVIDE]
    MONADIC_OPS = [COMMUTE]

    #注意我在文档中修改了几个常见的符号
    WYSIWYG = "+-*/()$"

    mapping = {
        "+" : PLUS,
        "-": MINUS,
        "*": TIMES, 
        "/": DIVIDE,
        "(": LPARENS,
        ")": RPARENS,
        "$": COMMUTE,
    }

    def __init__(self, type_, value) -> None:
        self.type = type_
        self.value = value
    
    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return self.__str__()


class Tokenizer:
    #右边到左进行操作的
    def __init__(self, code):
        
        self.code = code
        self.pos = len(self.code) - 1
        self.current_char = self.code[self.pos]
    
    def error(self, message):
        
        raise Exception(f"TokenizerError: {message}")

    def advance(self):
        
        self.pos -= 1
        self.current_char = None if self.pos < 0 else self.code[self.pos]

    def skip_whitespace(self):
        
        while self.current_char and self.current_char in " \t":
            self.advance()
    
    def get_integer(self):
        
        end_idx = self.pos

        while self.current_char and self.current_char.isdigit():
            self.advance()
        
        return self.code[self.pos+1 : end_idx+1]

    def get_number_token(self):
        
        parts = [self.get_integer()]

        if self.current_char == ".":
            self.advance()
            parts.append(".")
        
        num = "".join(parts[::-1])

        if "." in num:
            return Token(Token.FLOAT, float(num))
        else:
            return Token(Token.INTEGER, int(num))
    
    
    def get_wysiwyg_token(self):
        
        char = self.current_char
        
        if char in Token.mapping:
            self.advance()
            return Token(Token.mapping[char], char)
        
        self.error("Could not parse WYSIWYG token.")

    def get_next_token(self):
        
        self.skip_whitespace()
        
        
        if self.current_char == None:
            return Token(Token.EOF, None)

        if self.current_char in "0123456789":
            return self.get_number_token()

        if self.current_char in Token.WYSIWYG:
            return self.get_wysiwyg_token()
        
    def tokenize(self):
        
        tokens = [self.get_next_token()]

        while tokens[-1].type != Token.EOF:
            tokens.append(self.get_next_token())
        return tokens[::-1]

class ASTNode:




class Scalar(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = self.token.value

    def __str__(self):
        return f"S(self.value)"
    
    def __repr__(self):
        return self.__str__()


class Mop(ASTNode):
    def __init__(self, token, child):
        self.token = token
        self.child = child
        

