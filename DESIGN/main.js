const TokenType = {
    //操作符号系列

    //关键字系列
    DEFINE: "DEFINE",
    DECLARE: "DECLARE",
    
    //变量系列
    ID: "ID"
}


function idIsKeyWorld(id) {

    if (id in TokenType) {
        return id
    }

    return TokenType.ID; 
}

function token(type, literal) {
    this.type = type;
    this.literal = literal;
}

function lexer(src) {
    this.src = src;
}