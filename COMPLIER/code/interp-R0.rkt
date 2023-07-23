#lang racket
;;p->p'->p''->p'''

;;;;;;Node;;;;;;;;;;;;;;
(struct Int (value))
(struct Prim (op arg*))
(struct Read ())
(struct Add (left right))
(struct Neg (value))


;;;;;;;;;;;Program;;;;;;;
(struct Program (info e))


(define interp
    (lambda (e)
        (match e
            [(Int n) n]
            [(Prim 'read '())
                (define r (read))
                (cond [(fixnum? r) r]
                      [else (error 'interp-r1 "expected an integer" r)])]
            
            [(Prim '- (list e))
                (define v (interp e))
                (- 0 v)]

            [(Prim '+ (list e1 e2))
                (define v1 (interp e1))
                (define v2 (interp e2))
                (+ v1 v2)])))

(define interp-R0 
    (lambda (pro)
        (match pro
            [(Program info e) (interp e)])))