#lang racket

#| (let ([x 32])
    (let ([y 10])
        (+ x y))) |#

#| (let ([x.1 32])
    (let ([y.2 10])
        (+ x y))) |#


(define env '())

(define sign 0)

(define gensym
    (lambda (var)
        (set! sign (+ sign 1))
        (cons `(,var . ,sign))))

(define ext-env
    (lambda (x e env)
        (define var (gensym x))
        (cons `(,var . ,e) env)))


(define lookup
    (lambda (x env)
        (let ([p (assq x env)]
            (cond 
                [(not p) #f]
                [else (cdr p)])))))

;;--(define gensym
;;--    (fun ([:var Int] [-> pair])
;;          (Resutlt (cons `))))

;;如果在表达式中你就需要一种查找结构
;;structed recursion
;;environment

