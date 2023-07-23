正确的编译器:
```java
complie:     p -> x86 -> 42
interperter: p -> 42
```

```syntax
exp : int 
    | (read) 
    | (- exp)
    | (+ exp exp)
    | (- exp exp)
R0 ::= exp


exp : (Int int)
    | (Prim 'read '())
    | (Prim '- (list exp))
    | (Prim '+ (list exp exp))
    | var
    | (let ([var exp]) exp)
R0 : (Program '() exp)

reg : rsp ;;堆栈指针 
    | rbq
    | rsi
    | rdi
    | rax
    | ...
    | rdx
    | r8
    | ...
    | r15

arg : $int
    | %reg
    | int(%reg)

instr : addq arg, arg
      | subq arg, arg
      | negq arg
      | movq arg, arg
      | callq label
      | pushq arg
      | popq arg       ;;弹出栈
      | retq

prog : .globl main
            main: instr^{+}
```


```racket
(+ 10 32)


=>
;;到时候就照这个写
    .global main
main:
    movq $10, $rax
    addq $32, $rax
    movq %rax, %rdi
    callq print_int
    movq $0, %rax
    retq
```


编译器就是从一种编程语言转化成为另外一种编程语言
所有我们最开始应该比较两者的区别


uniquify: 重命名变量
variables shadowing <-> register addresses
not unique <-> unique

remove-complex-opera*: 通过引入临时变量来确保每个子表达式都是原子的
`+               <->  addq`

sub-expression       atomic args
```racket
(+ 10 (+ 1 2))

addq $10 %rax
```

explicate-controal: 从AST转化为控制流
两种求值顺序的不同
left  <-> jump


select-instructions: 将每个R1操作转化一系列指令
`+ <-> addq`

assign-home: 将变量替换成堆栈位置, 这一步可能是分配地址

variables <-> register 16
unbound <--> memory unbounded

patch-instructions
x86

----------------------------------------------
此pass为每个变量提供唯一的名称, 因此variable shadowing和scope就变得不重要了。

如果

```racket
(let ([x 32])
    (let ([y 10])
        (+ x y)))

(let ([x.1 32])
    (let ([y.1 10])
        (+ x.1 y.2)))

;;over shadowing
(let ([x 32])
    (+ (let ([x 10]) x) x))
```

在编译器中"gensym"是一种用于生成唯一标识符的技术。它通常用于编译器的内部实现，用于创建临时变量、重命名变量或生成其他唯一的符号名称。



remove-complex-opeara*
"nano-pass"
删除复杂的运算符和操作数

```racket
(+ (+ 42 10) (- 10))

=>
(let ([tmp.1 (+ 42 10)])
    (let ([tmp.2 (- 10)])
        (+ tmp.1 tmp.2)))

(let ([a 42]) 
    (let ([b a]))
        a)
=>
(let ([tmp.1 42])
    (let ([a tmp.1])
        (let ([tmp.2 a])
            (let ))))
```

需要在哪里进行递归, 注意观察语法树, 
注意是递归的结构往往不是原子的

需要做两个版本第一个版本就是说我需要做这件事情
我需要去递归, 另外一件事情说我不需要去递归

这两种情况往往是说一种是原子性的, 另外一种不是原子性的

```
RCO-ATOM : exp -> atom x (Var x exp) list vs1
RCO-EXP  : exp -> exp vs2

rco-atom:

(+ e1 e2)
(rco-atom e1) => a1 vs1
(rco-atom e2) => a2 vs2
(gensym 'tmp) => a3
return a3

(vs1, vs2, (x3, . (+ a1 a2)))
```

添加一个布尔标志, 来表示这个地方到底是原子还是表达式

explicate-control
因为我们在做增量

```

R1:
(let ([x (let ([y (- 42)]) y)])
 (- x))

R2:
    start:
        y = (-42);
        x = yi
        return (-x)
```

编译器的增量是一种优化技术, 用于减少在每次代码更改时重新编译整个程序时间和资源消耗。

传统上, 编译器在每次源代码发生变化的时候就会重新进行编译

```bnaf
CO atom : int | var
   
   exp  : atm | (read) | (- atom) | (+ atm atm)
   
   stmt : var = exp
   
   tail : retrun exp
        | stmt tail

C0 : start:
        tail

R1 : exp -> nt
         -> tail


R1 : tail

tail : atom | (read) | (-atom)
     | (let ([var nt]) tail)

nt : atm | (let ([var nt]) nt)

                 ->intail position R1
explicate-tail   : exp
explicate-assign : exp -> var
    -> tail x
```

```
(struct A
    (:a Int)
    (:b Int))
```